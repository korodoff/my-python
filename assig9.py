#Perform Inheritance 
class animal:
	def show(self):
		print("tiger")
class tiger(animal):
	def show(self):
		print("animal")
		super().show()
b=tiger()
b.show()
#Write The Output of a Code 
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())
#output will be:
#A B
#A B

#Create a Class Cope and Initialize it 
class Cop:
	def __init__(self,name,age,workexperience,designation):
		self.name=name
		self.age=age
		self.workexperience=workexperience
		self.designation=designation
	def show(self):
		print(" name:",self.name)
		print("age",self.age)
		print(" workexperience",self.workexperience)
		print("designation",self.designation)
	def update(self):
		self.name=input("update name")
		self.age=input("update age")
		self.workexperience=input("update workexperience")
		self.designation=input("enter designation")
class mission(Cop):
	def add_mission_details(self):
		self.mission=input("enter mission:")
		print(self.mission)
a=input("enter name:")
b=int(input("enter age:"))
c=input("enter workexperience:")
d=input("enter designation:")
print("\n")
x=mission(a,b,c,d)
x.show()
print("\n")
x.update()
print("\n")
x.show()
print("\n")
x.add_mission_details()
x.show()
#Create The Class Shape And Initialize It Initialize it
class shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def method_area(self):
		x=(self.length**2 or self.breadth**2)
		y=(self.length*self.breadth)
		print("area of square",x)
		print("area of reatangle",y)
class square_and_rectangle(shape):
		def show(self):
			return 'square_and_rectangle'
a=int(input("input length :"))
b=int(input("input breadth:"))
print("\n")
c=square_and_rectangle(a,b)
c.method_area()
