#Create a Circle Class and Initialize it with Radius.
class Circle:
	def __init__(self,radius):
		self.r=radius
		
	def getArea(self):
		print(self.r*self.r*3.14)
		
	def getCircumference(self):
		print(self.r*2*3.14)
		
c =Circle(2)

c.getArea()
c.getCircumference() 

#Create a Student Class and make Display And SetAge Method
class Student:
	def __init__(self,name,rollno):
		self.info=name
		self.n=rollno
	def show(self):
		print(self.info,self.n)
x=(input("enter name:"))
y=int(input("enter rollno:"))
s=Student(x,y)
s.show()
#Create a Temperature class. Make two Methods
class Temperature:
	def __init__(self,celsius,fahrenheite):
		self.n=celsius
		self.m=fahrenheite
	def show(self):
		print((self.n+32)*1.8)
		print((self.m-32)/1.8)
x=int(input("enter celsius"))
y=int(input("enter fahrenheite:"))
s=Temperature(x,y)
s.show()

#Create a Temperature class. Make two Methods
class MovieDetails:
	def __init__(self,name,artisname,yearofrelease,rating):
		self.l=name
		self.n=artisname
		self.m=yearofrelease
		self.o=rating
	def show(self):
		print(self.l,self.n,self.m,self.o)
	def update(self,name,artisname,yearofrelease,rating):
		self.l=name
		self.n=artisname
		self.m=yearofrelease
		self.o=rating
s2=MovieDetails("deadpool","ryan reynolds",2018,"9out of 10")
s2.show()
s2.update("transpoter","jason satham",2016,"8out of 10")
s2.show()

