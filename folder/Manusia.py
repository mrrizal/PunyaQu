class Manusia(object):
    def __init__(self, nama, alamat, umur):
        self.nama =  nama
        self.alamat = alamat
        self.umur = umur

    def getInfo(self):
        print("Nama : ",self.nama,"\nAlamat : ",self.alamat,"\nUmur : ",self.umur)

manusia1 = Manusia('Rizal','Jalan Bangbayang',20)
manusia1.getInfo()
