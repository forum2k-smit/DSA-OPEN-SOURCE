# Q-1::
# Create a Vehicle class with data member as maximum speed and
# mileage. Initialize their value by parameterised constructor
# function. Add a display function to display them.

'''
class vehicle():
	def __init__(self, speed, milage):
		self.speed=speed
		self.milage=milage

	def display(self):
		print("Speed=",self.speed)
		print("Milage=",self.milage)

obj=vehicle(100, 50)
obj.display()
'''

# Q-2::
# Create child class Bus that will inherit all of the variables and
# methods of the Vehicle class. Consider name_bus, Mileage_bus
# and speed_bus as the data member of the Vehicle class. Display
# all the information of the Bus
'''
class vehicle():
	def __init__(self, name_bus, milage_bus, speed_bus):
		self.name_bus=name_bus
		self.milage_bus=milage_bus
		self.speed_bus=speed_bus

	def display_info(self):
		print("Bus Name:"+self.name_bus)
		print("Bus Milage:",self.milage_bus)
		print("Bus Speed:",self.speed_bus)

class bus(vehicle):
	pass

obj=bus("Volvo", 100, 400)
obj.display_info()
'''

# Q-3::
# Create a Bus child class that inherits from the Vehicle class. The
# default fare charge of any vehicle is seating capacity * 100. If
# Vehicle is Bus instance, we need to add an extra 10% on full fare
# as a maintenance charge. So total fare for bus instance will
# become the final amount = total fare + 10% of the total fare.Note: The bus seating capacity is 50. so the final fare amount
# should be 5550. You need to override the fare() method of a
# Vehicle class in Bus class.

'''
class vehicle():
	def __init__(self, seating):
		self.seating=seating

	def fare(self):
		fare=self.seating*100
		print("The Fare of vehicle is",fare)

class bus(vehicle):
	def fare_bus(self):
		final=self.seating*100+(.1*self.seating*100)
		print("The fare of bus is",final) 

obj=bus(50)

obj.fare()
obj.fare_bus()
'''

# Q-4::
# Create a class called Invoice that a hardware store might use to
# represent an invoice for an item sold at the store. An Invoice
# should include four pieces of information as instance variables‐a
# part number, a part description, a quantity of the item being
# purchased and a price per item . Your class should have a
# constructor that initializes the four instance variables. Provide a
# set and a get method for each instance variable. In addition,
# provide a method named getInvoice Amount that calculates the
# invoice amount (i.e., multiplies the quantity by the price per
# item), then returns the amount as a double value. If the
# quantity is not positive, it should be set to 0. If the price per
# item is not positive, it should be set to 0.0. Write a test
# application named InvoiceTest that demonstrates class Invoice’s
# capabilities.
'''
class invoice:
	def __init__(self, number, descript, quantity, price_per_item):
		self.number=number
		self.descript=descript
		self.quantity=quantity
		self.price_per_item=price_per_item

	def getInvoice(self):
		if self.quantity < 0:
			self.quantity=0

		if self.price_per_item < 0.0:
			sel.price_per_item=0.0

		invoice=self.quantity * self.price_per_item
		return float(invoice)

InvoiceTest=invoice(2, "Wrench", 0, 20.0)

print("The invoice is ",InvoiceTest.getInvoice())

print("Number:",InvoiceTest.number)
print("Description:"+InvoiceTest.descript)
print("Quantity:",InvoiceTest.quantity)
print("Price per Item:",InvoiceTest.price_per_item)
'''

# Q-5::
# Create a class called Employee that includes three pieces of
# information as instance variables—a first name , a last name
# and a monthly salary. Your class should have a constructor that
# initializes the three instance variables. Provide a set and a get
# method for each instance variable. If the monthly salary is not
# positive, set it to 0.0. Write a test application named
# EmployeeTest that demonstrates class Employee’s capabilities.
# Create two Employee objects and display each object’s yearly
# salary. Then give each Employee a 10% raise and display each
# Employee’s yearly salary again.
'''
class employee:
	def __init__(self, fname="NULL", lname="NULL", mon_salary=0):
		self.fistname=fname
		self.lastname=lname
		self.mon_salary=mon_salary

	def get_fname(self):
		return self.firstname

	def set_fname(self, x):
		self.firstname=x

	def get_lname(self):
		return self.lastname

	def set_lname(self, y):
		self.lastname=y

	def get_mon_salary(self):
		return self.mon_salary

	def set_mon_salary(self, z):
		self.mon_salary=z

	def EmployeeTest(self):

		if self.mon_salary < 0:
			self.mon_salary = 0.0
		else:
			year_salary=12*self.mon_salary

		print("Yearly Salary=",year_salary,"of " +self.firstname +" " + self.lastname)
		per_raise=year_salary+(.1*year_salary)
		print("Ten Percent Increase=",per_raise,"of " +self.firstname +" " + self.lastname)

obj=employee()

obj.set_fname("Vivaan")
obj.set_lname("Shiromani")
obj.set_mon_salary(50000)
obj.EmployeeTest()

obj1=employee()

obj1.set_fname("Ram")
obj1.set_lname("Prasad")
obj1.set_mon_salary(60000)
obj1.EmployeeTest()
'''

# Q-6::
# Create a parent class called Car. The Car class has the following
# fields and methods: speed; regularPrice; color;
# doublegetSalePrice();
# 4) Create a sub class of Car class and name it as Truck. The Truck
# class has the following fields and methods: weight;
# getSalePrice();//Ifweight>2000,10%discount.Otherwise,20%discou
# nt.

"""
class car:
	def __init__(self, speed, regularPrice, color):
		self.speed=speed
		self.regularPrice=regularPrice
		self.color=color
	def doublegetSalePrice(self):
		pass

class truck(car):

	def __init__(self, weight, speed, regularPrice, color):
		self.weight=weight
		car.__init__(self, speed, regularPrice, color)
		self.speed=speed
		self.regularPrice=regularPrice
		self.color=color

	def getSalePrice(self):
		if self.weight > 2000:
			discount=self.regularPrice-(self.regularPrice*.1)
		else:
			discount=self.regularPrice-(self.regularPrice*.2)

		print("Regular Price:",self.regularPrice)
		print("Discounted Price:",discount)

obj=truck(3000, 100, 40000, "Red")

obj.getSalePrice()
"""
