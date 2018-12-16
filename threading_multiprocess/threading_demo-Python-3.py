#---------     Jai Hanumanji    Jai Ganeshji     Jai Laxmi-mataji     Jai Gurudev
#------------- Basic demo to threading module.

import threading
import time

def loop1_10():
    for i in range(1, 11):
        time.sleep(1)
        print(i)

t = threading.Thread(target=loop1_10)
t.start()
t.join()




#-------------- Implementing the same by inheriting the Thread class, Daemon thread

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              
        time.sleep(1)                         #mythread sleeps for 1 sec                   
        print("{} finished!".format(self.getName()))         

if __name__ == '__main__':
    for x in range(4):                                     
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # Initialize thread with name as Thread-(x+1)
        mythread.setDaemon(True)
        print("=======",mythread.isDaemon())
        mythread.start()                       # run() is called 
        time.sleep(5)                          #main-thread sleeps for 5 sec
        mythread.join()                        #main-thread waits until mythread finishes
        print("-------",mythread.isAlive())                        




#------------ Implementing the same above with __init__() method

import threading
import time

class MyThread(threading.Thread):
	def __init__(self):
		super(MyThread, self).__init__()
		# Can setup other parameters of thread before the thread starts
	def run(self):
		print ("Running",threading.current_thread().name)
		time.sleep(5)

thread_list = []
for i in range(4):
    thread = MyThread()            # Initialize through __init__()
    thread_list.append(thread)
    thread.setName("Thread "+str(i))
    thread.start()                 # run() is invoked
    print(thread.isAlive())
    thread.join()
    print("-------------",thread.isAlive())

print(thread_list)    #prints particular thread object as below
# [<MyThread(Thread 0, stopped 139836361111296)>, 
#  <MyThread(Thread 1, stopped 139836361111296)>, 
#  <MyThread(Thread 2, stopped 139836361111296)>, 
#  <MyThread(Thread 3, stopped 139836361111296)>]


