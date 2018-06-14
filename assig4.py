# i/p year and decide whether its leap year or not
l=int(input("enter year:"))
if(l%4==0):
  print("this is a leap year")
else:
  print("this is not a leap year")
 # check whether the userdefine length and breadth is square or rectangle
length=int(input("enter length:"))
breadth=int(input("enter breadth:"))
if(length==breadth):
 print("this is a square")
else:
 print("this is rectangle")
#Determine The Oldest And The Youngest People
person1=int(input("enter age1:"))
person2=int(input("enter age2:"))
person3=int(input("enter age3:"))
if(person1<person2):
 print("person1 is yongest")
elif(person2<person3):
 print("person2 is yongest")
else:
 print("person3 is yongest")
if(person1>person2):
 print("person1 is oldest")
elif(person2>person3):
 print("person2 is oldest")
else:
 print("person3 is oldest")
#Write an if statement to lets competitor know which of these prises they won.
n=int(input("rate messi from 1to 200:"))
if(1<=n<=50):
 print("Sorry! No prize this time")
elif(51<=n<=150):
 print("Congratulations! You won a wooden price") 
elif(151<=n<=180):
 print("Congratulations! You won a books")
elif(181<=n<=200):
 print("Congratulations! You won a Chocolates") 
#Print Total Cost after getting discount
quantity=int(input("quantity??:"))
print("discount of 10% over 1000")
if(quantity*100>1000):
 print("cost is",(quantity*100)-(10))
else:
 print("cost is",quantity*100 )  