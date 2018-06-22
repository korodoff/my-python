#Create a Threading Process 
import threading
from threading import Thread
import time
def display():
	time.sleep(5)
	print("child thread:",threading.current_thread())
t=Thread(target=display)
t.start()
print("main thread:",threading.current_thread())
#Make a Thread That Print Numbers 
import threading
from threading import Thread
import time
def display():
	for i in range(10):
		print("child thread:",threading.current_thread())
		time.sleep(1)
t=Thread(target=display)
t.setName("my thread")
t.start()
#Make a Thread for List of Three Elements
import threading
from threading import Thread
import time
def display():
	s=2
	for x in l:
		print(x)
		time.sleep(s)
		s=s+1
l=[1,2,3,4,5]
t=Thread(target=display)
t.start()
#Call Factorial Function using Thread.
import threading
from threading import Thread
def factorial():
	n=int(input("enter any no:"))
	fact=1
	for x in range(1,n+1): 
		fact=fact*x
		print("factorial is:"fact)
t=Thread(target=factorial)
t.start()