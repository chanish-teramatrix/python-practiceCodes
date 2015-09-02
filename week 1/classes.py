class car(object):
	def __init__(self,brand,model):
		self.brand = brand
		self.model = model

	@staticmethod
	def carsound():
		print "vroooomvrooooooom"
	
	@classmethod
	def total_seat(self,seats):
		self.seats = seats
		print "total no. of seats are: ",self.seats

car.carsound()
figo = car('ford','figo_basic')
figo.total_seat(5)
figo.carsound()
