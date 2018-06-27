#Write a Python program to read last n lines of a file
f=open('q1.txt','r')
z=int(input("enter line you want to print:"))
c=f.readlines()
while z:
	print(c[-z])
	z=z-1
f.close

#Write a Python program to count the frequency of words in a file
c=0
f=open('q1.txt','r')
for lines in f:
 words=lines.split()
 c += len(words)
print(c)
f.close
#WAP Python program to copy the contents of a file
with open('q1.txt','r') as f:
 with open('q3.txt','w') as d:
		for line in f:
			d.write(line)
		c=f.readline()
		print(c)

#Write a Python program to combine each line from first file
with open('q1.txt','r') as f:
 with open('q3.txt','r') as d:
  for line1,line2 in (f,d):
  print(line1+line2)


import os
import random
random_list=[]
for x in range(100):
    random_list.append(x)
random.shuffle(random_list)
with open("q4.txt","w") as f1:
    for x in range(10):
        f1.write(str(random_list[x])+"\n")
os.remove("q41.txt")
with open("q4.txt","r+") as f1:
    with open("q41.txt","w") as f2:
        random_list1=f1.readlines()
        for x in range(len(random_list1)):
            random_list1[x]=int(random_list1[x])
        random_list1.sort()
        # f2.write("".join(random_list1))
        for x in random_list1:
            f2.write(str(x)+"\n") 