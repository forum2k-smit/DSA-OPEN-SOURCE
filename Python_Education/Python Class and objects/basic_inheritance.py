"""
Use of basic inhertance in python.
"""

"""
Here peron is the parent class and student is child class which is inheriting all 
functions of person class. 
"""
# Uncomment to test. 

"""
class person():
	def __init__(self, fname, lname):
		self.firstname=fname
		self.lastname=lname

	def display(self):
		print(self.firstname,self.lastname)

class student(person):
	def __init__(self, fname, lname, year):
		super().__init__(fname,lname)
		self.graduation=2019
		self.year=year

	def display_details(self):
		print(self.year,self.firstname,self.lastname,self.graduation)

x=student("xyz","abc",2014) # This is object defination calling the init function of child i.e student.

x.display() # This is parent class method calling.

x.display_details() # This is child class method calling.

print(x.year)  # This is printing the data member of child class with a value in object defination-2014.

print(x.graduation) # This is printing the data member of child class with value added already.
"""