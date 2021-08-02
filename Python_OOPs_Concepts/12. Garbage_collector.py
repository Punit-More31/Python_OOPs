#  GARGAGE COLLECTOR 
''' The main objective of garbage collector is to destry useless object.To perform resourse deallocation GC calls
Just before destroying an objct, GC always calls destructor to perform cleanup activities.
GC is involked by python Virtual machine

1.The purpose of destuctor to destroy useless objects
2.The purpose of destuctor is to perform cleaup activities before destroying an object
 

'''

import gc                       #garbage Collector
print(gc.isenabled())#True
gc.disable()
print(gc.isenabled())#false
gc.enable()
print(gc.isenabled())#True

print('--------------------------------------------')
#Before terminating a program all the object which is of no use are destroyed

import time
class Test:
    def __init__(self):
        print('Object Initiolization..')
    
    def __del__(self):
        print('Fulfulling last wish and perforimng cleanup Activies...')

gc.disable()
print(gc.isenabled())
t1 = Test()
t1 =None
#del t1
time.sleep(5)
print('End of application')

print("-----------------------------------------------")

t1 = Test()
t2 = t1
t3 = t2
t4 = t3
print("-----------------------------------")
import sys
print("no of reference variable:", sys.getrefcount(t1))#t1,t2,t3,t4,and self i.e 5 refernce variable
print("-----------------------------------")
del t1
time.sleep(5)
print('After deleting t1 object not destroyed')
del t2
del t3
time.sleep(5)
print('still object not eligible for gc')
time.sleep(5)
del t4
time.sleep(5)
print("End of application")
print("-----------------------------------------")

list[Test(),Test(),Test()]
time.sleep(5)
# list.None

 
 