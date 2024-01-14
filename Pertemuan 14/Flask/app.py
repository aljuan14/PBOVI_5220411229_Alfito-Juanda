from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, data=None):
        self.cursor.execute(query, data)
        self.connection.commit()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, data):
        self.cursor.execute(query, data)
        return self.cursor.fetchone()

class Mahasiswa:
    def __init__(self, db):
        self.db = db

    def add_data(self, npm, nama, jurusan):
        query = "INSERT INTO data_mahasiswa (npm, nama, jurusan) VALUES (%s, %s, %s)"
        data = (npm, nama, jurusan)
        self.db.execute_query(query, data)

    def get_all_data(self):
        query = "SELECT * FROM data_mahasiswa"
        return self.db.fetch_all(query)

    def get_data_by_npm(self, npm):
        query = "SELECT * FROM data_mahasiswa WHERE npm = %s"
        data = (npm,)
        return self.db.fetch_one(query, data)

    def update_data(self, npm, nama, jurusan):
        query = "UPDATE data_mahasiswa SET nama=%s, jurusan=%s WHERE npm=%s"
        data = (nama, jurusan, npm)
        self.db.execute_query(query, data)

    def delete_data(self, npm):
        query = "DELETE FROM data_mahasiswa WHERE npm=%s"
        data = (npm,)
        self.db.execute_query(query, data)

# Konfigurasi Database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': '5220411229'
}

# Inisialisasi Objek Database dan Mahasiswa
database = Database(**db_config)
mahasiswa_manager = Mahasiswa(database)

@app.route('/add', methods=['POST'])
def add_data():
    npm = request.form['npm']
    nama = request.form['nama']
    jurusan = request.form['jurusan']

    mahasiswa_manager.add_data(npm, nama, jurusan)

    return redirect('/')

@app.route('/')
def index():
    data_mahasiswa = mahasiswa_manager.get_all_data()
    return render_template('index.html', data_mahasiswa=data_mahasiswa)

@app.route('/edit/<int:npm>', methods=['GET'])
def edit_data(npm):
    mahasiswa = mahasiswa_manager.get_data_by_npm(npm)
    return render_template('edit.html', mahasiswa=mahasiswa)

@app.route('/update/<int:npm>', methods=['POST'])
def update_data(npm):
    nama = request.form['nama']
    jurusan = request.form['jurusan']

    mahasiswa_manager.update_data(npm, nama, jurusan)

    return redirect('/')

@app.route('/delete/<int:npm>')
def delete_data(npm):
    mahasiswa_manager.delete_data(npm)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
