#Create a Function To Calculate Area of a circle
r=int(input("enter radius of a circle:"))
def area():
 x=3.14
 z=x*r**2
 print("area of a circle is:",z)
area()
   
 #Q3 Print multiplication table of 12 using recursion		

def table(n):
	if n>10:
		return n
	else:
		print(12*n)
		table(n+1)
table(1)
print("\n")	

#4 Write a function to calculate power of a number raised to other ( a^b ) using recursion	

def power (n,p):
	s = 1
	if (p ==1):
		return n 
	else:
		s = n*power(n,p-1)
		return s
print(power(5,3))		
		
print("\n")			
	
	

#Q5 Write a function to find factorial of a number but also store the factorials calculated in a dictionary
	
def fact (x):
	if x==1:
		return 1
	else:
		x = x*fact(x-1)
		return x
a = int(input("enter a number: "))
f = fact(a)	
print(f)
d = [()]
d.append(f)
print(d) 