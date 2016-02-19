from Manusia import Manusia

class Mahasiswa(Manusia):
    def __init__(self, nama, alamat, umur, universitas):
        super(Mahasiswa, self).__init__(nama, alamat, umur)
        self.universitas = universitas

    def getInfo(self):
        print("nama : ",self.nama,"\nalamat :",self.alamat,"\numur : ",self.umur,"\nuniversitas : ",self.universitas)



mahasiswa1 = Mahasiswa('rizal','Jalan Bangbayang',20,'STMIK LIKMI')
mahasiswa1.getInfo()
