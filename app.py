from pickle import TRUE
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

application = Flask(__name__)
#Memanggil file config
application.config.from_pyfile('config.cfg')
application.config['SECRET_KEY'] = '@#$123456&*()'
#Mengoneksikan dengan database, menggunakan MySQL Alchemy
application.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:''@localhost/uts_python'
application.config['SQLALCHEMY_TRACK_MODIFICATION'] = TRUE

#Mendefinisikan SQL Alchemy kedalam variable db
db = SQLAlchemy(application)

#Membuat Class Model Buku
class Buku(db.Model):
    __tablename__ = 'buku'
    kode_buku = db.Column(db.String(5), primary_key = True)
    judul = db.Column(db.String(100))
    stok = db.Column(db.String(10))

    def __init__(self, kode_buku, judul, stok):
        self.kode_buku = kode_buku
        self.judul = judul
        self.stok = stok

    def __repr__(self):
        return '[%s,%s,%s]' % \
            (self.kode_buku, self.judul, self.stok)

#Membuat Class Model Anggota
class Anggota(db.Model):
    __tablename__ = 'anggota'
    nim = db.Column(db.String(10), primary_key = True)
    nama_mahasiswa = db.Column(db.String(100))
    jurusan = db.Column(db.String(50))

    def __init__(self, nim, nama_mahasiswa, jurusan):
        self.nim = nim
        self.nama_mahasiswa = nama_mahasiswa
        self.jurusan = jurusan

    def __repr__(self):
        return '[%s,%s,%s]' % \
            (self.nim, self.nama_mahasiswa, self.jurusan)

#Membuat Class Model Peminjaman
class Peminjaman(db.Model):
    __tablename__ = 'pinjam'
    kode_pinjam = db.Column(db.String(5), primary_key = True)
    kode_buku = db.Column(db.String(5))
    nim = db.Column(db.String(10))
    tgl_pinjam = db.Column(db.Date())

    def __init__(self, kode_pinjam, kode_buku, nim, tgl_pinjam):
        self.kode_pinjam = kode_pinjam
        self.kode_buku = kode_buku
        self.nim = nim
        self.tgl_pinjam = tgl_pinjam

    def __repr__(self):
        return '[%s,%s,%s,%s]' % \
            (self.kode_pinjam, self.kode_buku, self.nim, self.tgl_pinjam)

#Membuat Class Model Pengembalian
class Pengembalian(db.Model):
    __tablename__ = 'kembali'
    kode_kembali = db.Column(db.String(5), primary_key = True)
    kode_buku = db.Column(db.String(5))
    nim = db.Column(db.String(10))
    tgl_kembali = db.Column(db.Date())

    def __init__(self, kode_kembali, kode_buku, nim, tgl_kembali):
        self.kode_kembali = kode_kembali
        self.kode_buku = kode_buku
        self.nim = nim
        self.tgl_kembali = tgl_kembali

    def __repr__(self):
        return '[%s,%s,%s,%s]' % \
            (self.kode_kembali, self.kode_buku, self.nim, self.tgl_kembali)

#Membuat Class Model Users
class Users(db.Model):
    __tablename__ = 'users'
    nama = db.Column(db.String(50))
    email = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String(50))

    def __init__(self, nama, email, password):
        self.nama = nama
        self.email = email
        self.password = password

    def __repr__(self):
        return '[%s,%s,%s]' % \
            (self.nama, self.email, self.password)

@application.route('/')
def index():
    return render_template('login.html',
    head = application.config['HEAD'],
    menu = application.config['MENU'],   
    footer = application.config['FOOTER']
    )

@application.route('/home')
def home():
    return render_template('index.html',
    head = application.config['HEAD'],
    menu = application.config['MENU'],   
    footer = application.config['FOOTER']
    )

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Menggambil nilai dari form html, dimasukkan kedalam variable
        email = request.form['email']
        password = request.form['password']
        users = Users.query.filter_by(email=email).first()
        if (users.email != email) or (users.password != password):
            flash('Email or Password Invalid !!')
        else:
            return redirect(url_for('home'))

    return render_template('login.html',
    head = application.config['HEAD'],
    menu = application.config['MENU'],   
    footer = application.config['FOOTER']
    )

#Menambahkan Data ke Table Users (Create)
@application.route('/register', methods=['GET', 'POST'])
def register():
    #Menggunakan try except agar saat user input email(primary key) yang sudah ada
    #maka website tidak error, tetapi akan ada pesan bahwa email sudah ada
    try:
        if request.method == 'POST':
            #Menggambil nilai dari form html, dimasukkan kedalam variable
            nama = request.form['nama']
            email = request.form['email']
            password = request.form['password']
        #Memasukkan bbrp variable tadi kedalam Buku dengan parameter kodebuku, judul, dan stok
            users = Users(nama,email,password)
            #Mengirim data ke database
            db.session.add(users)
            db.session.commit()
            flash('Registrasi Berhasil !!') #Memberikan alert bahwa data berhasil ditambah
            return redirect(url_for('login')) #Akan dikembalikan ke halaman daftarbuku
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        flash('Email Sudah Terdaftar !!')
        return redirect(url_for('login'))
    
    return render_template('login.html',\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

@application.route('/logout')
def logout():
    flash('Logout Berhasil !!')
    return render_template('login.html',
    head = application.config['HEAD'],
    menu = application.config['MENU'],
    footer = application.config['FOOTER']
    )

###############################################################################################
                                        #BUKU#

#Menampilkan Data dari Table Buku (Read)
@application.route('/buku')
def daftarBuku():
    #Ketika Route Buku dipanggil, maka template yang dirender adalah daftar_buku, 
    #beserta data2 dari model Buku
    return render_template('daftar_buku.html', container=Buku.query.all(),\
    #Memanggil head pada html, Menu/navbar, dan footer yang dibuat pada Config
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Menambahkan Data ke Table Buku (Create)
@application.route('/addbuku', methods=['GET', 'POST'])
def addBuku():
    #Menggunakan try except agar saat user input kode_buku(primary key) yang sudah ada
    #maka website tidak error, tetapi akan ada pesan bahwa kode buku sudah ada
    try:
        if request.method == 'POST':
            #Menggambil nilai dari form html, dimasukkan kedalam variable
            kode_buku = request.form['kode_buku']
            judul = request.form['judul']
            stok = request.form['stok']
        #Memasukkan bbrp variable tadi kedalam Buku dengan parameter kodebuku, judul, dan stok
            buku = Buku(kode_buku,judul,stok)
            #Mengirim data ke database
            db.session.add(buku)
            db.session.commit()
            flash('Data Berhasil Ditambah') #Memberikan alert bahwa data berhasil ditambah
            return redirect(url_for('daftarBuku')) #Akan dikembalikan ke halaman daftarbuku
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        flash('Kode Buku sudah ada!!')
        return redirect(url_for('addBuku'))
    
    return render_template('add_buku.html',\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Mengubah data yang ada pada Table Buku (Update)
@application.route('/editbuku/<kode_buku>', methods=['GET', 'POST'])
def editBuku(kode_buku):
    #Mencari data yang sesuai dengan parameter kodebuku yang dikirim
    buku = Buku.query.filter_by(kode_buku=kode_buku).first()
    if request.method == 'POST':
        #Menimpa data pada variable buku.{variable} kemudian diambil dari form html
        buku.judul = request.form['judul']
        buku.stok = request.form['stok']
        #Mengirim data yang sudah diupdate kedalam database sql
        db.session.add(buku)
        db.session.commit()
        #Memberikan alert bahwa data berhasil diubah
        flash('Data buku dengan judul : '+ str(buku.judul)+ ', Berhasil Diubah')
        #Mengembalikan ke halaman daftar buku
        return redirect(url_for('daftarBuku'))
    else:

        return render_template('edit_buku.html', container=buku,\
        head = application.config['HEAD'],\
        menu = application.config['MENU'],\
        footer = application.config['FOOTER']
        )

#Menghapus data pada Table Buku (Delete)
@application.route('/deletebuku/<kode_buku>', methods = ['GET', 'POST'])
def deleteBuku(kode_buku):
    try:
        #Mencari data dengan kode buku yang diterima
        buku= Buku.query.filter_by(kode_buku=kode_buku).first()
        #Menghapus data yang dicari, karena kode buku primary, maka data yang dicari otomatis hanya 1
        #Maka data tersebut dihapus menurut kodebukunya
        db.session.delete(buku)
        db.session.commit()
        flash('Data Berhasil Dihapus') #Memberikan alert berhasil dihapus
        return redirect(url_for('daftarBuku')) #Mengembalikan ke halaman daftar buku
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        flash('Buku Masih dalam Peminjaman/Belum Dikembalikan')
        return redirect(url_for('daftarBuku'))


###############################################################################################
                                        #ANGGOTA#

#Menampilkan Data dari Table Anggota (Read)
@application.route('/anggota')
def daftarAnggota():
    return render_template('daftar_anggota.html', container=Anggota.query.all(),\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Menambahkan Data ke Table Anggota (Create)
@application.route('/addanggota', methods=['GET', 'POST'])
def addAnggota():
    try:
        if request.method == 'POST':
            nim = request.form['nim']
            nama_mahasiswa = request.form['nama_mahasiswa']
            jurusan = request.form['jurusan']
            anggota = Anggota(nim,nama_mahasiswa,jurusan)
            db.session.add(anggota)
            db.session.commit()
            flash('Data Berhasil Ditambah')
            return redirect(url_for('daftarAnggota'))
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        flash('NIM sudah ada!!')
        return redirect(url_for('addAnggota'))
    
    return render_template('add_anggota.html',\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Mengubah data yang ada pada Table Anggota (Update)
@application.route('/editanggota/<nim>', methods=['GET', 'POST'])
def editAnggota(nim):
    anggota = Anggota.query.filter_by(nim=nim).first()
    if request.method == 'POST':
        anggota.nama_mahasiswa = request.form['nama_mahasiswa']
        anggota.jurusan = request.form['jurusan']
        db.session.add(anggota)
        db.session.commit()
        flash('Data Anggota : '+ str(anggota.nama_mahasiswa)+ ', Berhasil Diubah')
        return redirect(url_for('daftarAnggota'))
    else:

        return render_template('edit_anggota.html', container=anggota,\
        head = application.config['HEAD'],\
        menu = application.config['MENU'],\
        footer = application.config['FOOTER']
        )

#Menghapus data pada Table Anggota (Delete)
@application.route('/deleteanggota/<nim>', methods = ['GET', 'POST'])
def deleteAnggota(nim):
    anggota= Anggota.query.filter_by(nim=nim).first()
    db.session.delete(anggota)
    db.session.commit()
    flash('Data Berhasil Dihapus')
    return redirect(url_for('daftarAnggota'))

#################################################################################################
                                    #PeminjamanBuku#

#Menampilkan Data dari Table Pinjam (Read)
@application.route('/peminjaman')
def daftarPeminjaman():
    return render_template('daftar_peminjaman.html', container=Peminjaman.query.all(),\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Menambahkan Data ke Table Pinjam (Create)
@application.route('/addpeminjaman', methods=['GET', 'POST'])
def addPeminjaman():
    try:
        if request.method == 'POST':
            kode_pinjam = request.form['kode_pinjam']
            kode_buku = request.form['kode_buku']
            nim = request.form['nim']
            tgl_pinjam = request.form['tgl_pinjam']
            peminjaman = Peminjaman(kode_pinjam,kode_buku,nim,tgl_pinjam)
            #Mengurangi Stok dengan kode buku yang dipinjam
            buku = Buku.query.filter_by(kode_buku=kode_buku).first()
            if (int(buku.stok) > 0): 
                buku.stok = int(buku.stok) - 1
                db.session.add(peminjaman)
                db.session.commit()
                db.session.add(buku)
                db.session.commit()
                flash('Buku Berhasil Dipinjam')
                return redirect(url_for('daftarPeminjaman'))
            else:
                flash('Stok Habis !!')
                return redirect(url_for('addPeminjaman'))
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        flash('Kode Pinjam sudah ada!!')
        return redirect(url_for('addPeminjaman'))
    
    return render_template('add_peminjaman.html', container=Buku.query.all(), container1=Anggota.query.all(),\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Menghapus data pada Table Anggota (Delete)
@application.route('/deletepeminjaman/<kode_pinjam>', methods = ['GET', 'POST'])
def deletePeminjaman(kode_pinjam):
    peminjaman= Peminjaman.query.filter_by(kode_pinjam=kode_pinjam).first()
    db.session.delete(peminjaman)
    db.session.commit()
    ##Menambahkan Stok kembali ketika daftar peminjaman dihapus
    kode_buku = peminjaman.kode_buku
    buku = Buku.query.filter_by(kode_buku=kode_buku).first()
    buku.stok = int(buku.stok) + 1
    db.session.add(buku)
    db.session.commit()
    flash('Peminjaman Buku Berhasil Dihapus')
    return redirect(url_for('daftarPeminjaman'))

#################################################################################################
                                    #PengembalianBuku#

#Menampilkan Data dari Table Kembali (Read)
@application.route('/pengembalian')
def daftarPengembalian():
    return render_template('daftar_pengembalian.html', container=Pengembalian.query.all(),\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Menambahkan Data ke Table Kembali (Create)
@application.route('/addpengembalian', methods=['GET', 'POST'])
def addPengembalian():
    try:
        if request.method == 'POST':
            kode_kembali = request.form['kode_kembali']
            kode_buku = request.form['kode_buku']
            nim = request.form['nim']
            tgl_kembali = request.form['tgl_kembali']
            pengembalian = Pengembalian(kode_kembali,kode_buku,nim,tgl_kembali)
            db.session.add(pengembalian)
            db.session.commit()
            #Mengurangi Stok dengan kode buku yang dipinjam
            buku = Buku.query.filter_by(kode_buku=kode_buku).first()
            buku.stok = int(buku.stok) + 1
            db.session.add(buku)
            db.session.commit()
            flash('Buku Berhasil Dikembalikan')
            return redirect(url_for('daftarPengembalian'))
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        flash('Kode Kembali sudah ada!!')
        return redirect(url_for('addPengembalian'))
    
    return render_template('add_pengembalian.html', container=Buku.query.all(), container1=Anggota.query.all(),\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

#Menghapus data pada Table Anggota (Delete)
@application.route('/deletepengembalian/<kode_kembali>', methods = ['GET', 'POST'])
def deletePengembalian(kode_kembali):
    pengembalian= Pengembalian.query.filter_by(kode_kembali=kode_kembali).first()
    ##Menambahkan Stok kembali ketika daftar peminjaman dihapus
    kode_buku = pengembalian.kode_buku
    buku = Buku.query.filter_by(kode_buku=kode_buku).first()
    if (int(buku.stok) > 0): 
        db.session.delete(pengembalian)
        db.session.commit()
        buku.stok = int(buku.stok) - 1
        db.session.add(buku)
        db.session.commit()
        flash('Pengembalian Buku Berhasil Dihapus')
        return redirect(url_for('daftarPengembalian'))
    else:
        flash('Penghapusan Pengembalian Tidak Bisa Diproses, Stok Buku Habis')
        return redirect(url_for('daftarPengembalian'))

#################################################################################################
                                        #AboutUs#

#Menampilkan Halaman About Us
@application.route('/about')
def about():
    return render_template('about_us.html',\
    head = application.config['HEAD'],\
    menu = application.config['MENU'],\
    footer = application.config['FOOTER']
    )

if __name__ == '__main__':
    application.run(debug=True)