'''Process based Multi tasking:
-----------------------------------------

Each task is a seperate independent process

typing a python program in the editor
listerning an audio songs from the same system
Downloading new songs from the internet

OS level 

2.Thread based multi tasking:
--------------------------------------------
Each tasks is independent part of same program
An idependent part of program
A flow of execution is considered as a thread
It is a python object

three ways:
1. creating a thread without using any class
2. creating a thread by extending thread class
3. Creating a thread without extending thread class

1. Creating a thread without using any class:

 
'''

# import threading
# print('current Executing thread:', threading.current_thread().getName())


from threading import *
def disply():
    for i in range(10):
        print('Child Thread')
t = Thread(target=disply) #creating of thread object to execute display