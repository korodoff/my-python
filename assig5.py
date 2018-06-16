#Take a Input From User and Print On Screen
n=1
while n<=10:
   c=int(input("enter any no"))
   n=n+1    
   print(c)
#Write an Infinite Loop
n=1
while n<=10:    
  print("din't i ever tell you the defination of insanity")    

#Create a List of Integers And Make a New List 
l=[]
l.append(int(input("enter integer")))
l.append(int(input("enter integer")))
l.append(int(input("enter integer")))
l1=[]

for x in l:
	l1.append(x**2)

print(l)
print(l1)	
#From a list for Integer,Float and String
l=[1,'a',1.3,2,'b',2.5]
l1=[]
l2=[]
l3=[]
for x in l:
	if type (x)==int:
	 l1.append(x)
	elif type (x)==float:
	 l2.append(x)
	elif type(x)==str:
	 l3.append(x)
print(l1)
print(l2)
print(l3)
#using range(1,1o1)make a list containing even and odd numbers.
l=[]
l1=[]
for x in range(1,101):
 if(x%2==0):
  l.append(x)
 else:
  l1.append(x)
print(l)
print(l1)   
# print patterns
for i in range(0,5):
  for j in range(0,i+1):
   print("*",end="")
  print()
  #Create a User Defined Dictionary
d={}
for i in range(0,3):
 text=input("enter char and int ").split()
 d[text[0]]=text[1]
print(d)
#Perform Inputs And Search and deletion From User in a list
l=[]
for i in range(0,5):
  l.append(input("enter list:"))
print(l)
l1=[]
l1.append(input("enter to search remove element from list:"))
print(l1)
for x in l:
 if x in l1:
  l.remove(x)
print(l)   