class Segitiga:
	
	def __init__(self, tinggi, alas):
		self.tinggi = tinggi
		self.alas = alas
		
	
	def getLuas(self):
		return self.tinggi*self.alas/2
		
segitiga1 = Segitiga(10,2)
print(segitiga1.getLuas())
		
	
