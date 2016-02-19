class Manusia(object):
    def __init__(self, nama, alamat, umur):
        self.nama =  nama
        self.alamat = alamat
        self.umur = umur

    def getInfo(self):
        print("Nama : ",self.nama,"\nAlamat : ",self.alamat,"\nUmur : ",self.umur)

class Mahasiswa(Manusia):
    def __init__(self, nama, alamat, umur, universitas):
        super(Mahasiswa, self).__init__(nama, alamat, umur)
        self.universitas = universitas

    def getInfo(self):
        print("nama : ",self.nama,"\nalamat :",self.alamat,"\numur : ",self.umur,"\nuniversitas : ",self.universitas)



mahasiswa1 = Mahasiswa('rizal','Jalan Bangbayang',20,'STMIK LIKMI')
mahasiswa1.getInfo()
