class Currency(object):

	def __init__(self, currency_type):
		pass

	def convert(self):
		pass

class Dollar(Currency):

	def convert(self):
		pass

class Euro(Currency):

	def convert(self):
		pass

class Distance(object):

	def convert(self):
		pass

class Kilometer(Distance):

	def convert(self):
		pass

class Mile(Distance):

	def convert(self):
		pass

class Person(object):
	
	def __init__(self, name):
		self.name = name
		pass

class City(object):

	def __init__(self, starting_city=False):
		self._starting_city = starting_city
		pass

	def activity(self):
		pass

	def airport_code(self):
		pass

class Frankfurt(City):

	def activity(self):
		pass

	def airport_code(self):
		pass

class Stuttgart(City):

	def activity(self):
		pass

	def airport_code(self):
		pass

class Munchen(City):

	def activity(self):
		pass

	def airport_code(self):
		pass

class Berlin(City):

	def activity(self):
		pass

	def airport_code(self):
		pass

class Chicago(City):

	def activity(self):
		pass

class Nashville(City):

	def activity(self):
		pass

class Rostock(City):

	def activity(self):
		pass

class Lubeck(City):

	def activity(self):
		pass

class Hamburg(City):

	def activity(self):
		pass

class Bremen(City):

	def activity(self):
		pass

class Hannover(City):

	def activity(self):
		pass

class Kassel(City):

	def activity(self):
		pass

class Dusseldorf(City):

	def activity(self):
		pass

class Koln(City):

	def activity(self):
		pass

class St(City):

	def activity(self):
		pass

class Bonn(City):

	def activity(self):
		pass

class Wiesbaden(City):

	def activity(self):
		pass

class Mannheim(City):

	def activity(self):
		pass

class Karlsruhe(City):

	def activity(self):
		pass

class Baden_Baden(City):

	def activity(self):
		pass

class Nurnberg(City):

	def activity(self):
		pass

class Dresden(City):

	def activity(self):
		pass

class Leipzig(City):

	def activity(self):
		pass

class Basel(City):

	def activity(self):
		pass
		
class Fuel(object):

	def __init__(self):
		pass

	def fuel_mileage(self):
		pass

class Diesel(Fuel):

	def fuel_mileage(self):
		pass

class Petrol(Fuel):

	def fuel_mileage(self):
		pass

class Vehicle(object):

	fuels = {
		'diesel': Diesel(),
		'petrol': Petrol()
	}

	def __init__(self, fuel_type):
		fuel = Vehicle.fuels.get(fuel_type)
		self.fuel_type = fuel
		print "Fuel type", self.fuel_type

	def cost(self):
		pass

class Car(Vehicle):

	def cost(self):
		pass

class Train(Vehicle):

	def cost(self):
		pass

class Taxi(Vehicle):
	
	def cost(self):
		pass

a_vehicle = Car('petrol')
