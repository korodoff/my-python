#ASSIGMENT-2(datatypes-1)

# create a list and add other list to it.
l=[1]
l[0]=input("enter any:")
print(l)
l1=['google','apple','facebook','microsoft','telsa']
print(l.extend(l1))
print(l)
# count no of element
l=[1,4,5,2,1,3,1]
print(l.count(1))
# sortion of unordered list
a=[4,2,1,6,5]
a.sort()
print(a)
# merging of 2 one-dimenional list in acending ordered
a=[4,7,8,5,4]
b=[1,3,6,2]
a.sort()
b.sort()
print(a,b)
print(a.extend(b))
a.sort()
print(a)
#implementing of stack and queue

stack = ["tristam", "aerochord", "dillon"]
print(stack)
stack.append("fluxpavilion")
stack.append("panda")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

queue =(["tristam", "aerochord", "dillon"])
print(queue)
queue.append("fluxpavilion")
queue.append("panda")
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

#count even and odd element
no=(1,2,3,4,5)
count_odd=0
count_even=0
for a in no:
  if a % 2:
    count_even+=1
  else:
   count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


#ASSIGMENT-1(intro to python)
#print anything on screen
x=input("print anything you want on the screen:")
print(x)

#addition of two string
x="LA"
y="ME"
z=x+y
print(z)

# enter 3 variable
print("enter these three information")
p=input("name:")
q=int(input("phno:"))
r=input("password:")
print("%s %d %s"%(p,q,r))

# print let get started
print("ok now let's get started")

#print following value using placeholders
s="acadview"
cource="python"
fees="6000"
print("welcome to "+s+" where we teach "+cource+" for only "+str(fees)+" rupees")

# bonus question
x=100000
y="tony stark"
print("%d %s"%(x,y,))
