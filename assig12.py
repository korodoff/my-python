#Name and handle the Exception Occured in a Program
#ZeroDivisionError
try:
 a=3
 if a<4:
  a=a/(a-3)
  print(a)
except ZeroDivisionError:
  print("ZeroDivisionError occur")

#Name and handle the Exception Occured in a Program
#IndexError
try:
 l=[1,2,3]
 print(l[3])
except IndexError:
 print("IndexError occur")

#Find The Output Of a Code
try:
	raise NameError("hi there")
except NameError:
	print("An exception")
	raise
# out put will be:
# raise NameError("hi there")
# NameError: hi there

#Find The Output Of a Code
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
# out put will be:
# -5.0
# a/b result in 0

# Import Error
try:
 raise ImportError
except ImportError:
 print("import error occur")
#  ValueError
try:
 raise ValueError
 print("any")
except ValueError:
 print("value error occur")
# IndexError
l=[1,2]
try:
  print(l[4])
except IndexError:
 print("IndexError occur")
#Create a user-defined exception 
class AgeTooSmallError(Exception):
	pass
age=0
while age<18:
	age=int(input("enter your age=>"))
	try:
		if age<18:
			raise AgeTooSmallError("age is too small try again")
	except Exception as e:
		print(e)