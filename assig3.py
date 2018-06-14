# find length of tuple
t=(1,2,3,4,'q','r')
print(t)
print(len(t))
#largest and smallest in tuple
t=(1,2,3,4,5,6)
print(t)
print("max number is: ",max(t))
print("min number is:",min(t))
#product af all element of tuple
t=(1,2,3,4,5)
k=t[0]*t[1]*t[3]*t[4]
print(k)
#sets create,differenceand intersection of a set
n=set(input("enter element1:"))
m=set(input("enter element2:"))
print(n)
print(m)
print("differrence between two set",n - m)
print("intersection between two set",n & m)

#create dictionary to store no of names and marks and sort the list
d={}
v=[]
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
name=input("enter your name")
marks=int(input("enter marks"))
d[name]=marks
v.append(marks)
print(d)
#here we take list since we cannot convert a dictionary 
print(v)
v.sort()
print(v)
#count a no of occurrece of each letter in MISSISSIPPI
l=list("mississippi")
d={}
d['m']=l.count('m')
d['i']=l.count('i')
d['s']=l.count('s')
d['s']=l.count('s')
d['i']=l.count('i')
d['s']=l.count('s')
d['s']=l.count('s')
d['i']=l.count('i')
d['p']=l.count('p')
d['p']=l.count('p')
d['i']=l.count('i')
print(d)

