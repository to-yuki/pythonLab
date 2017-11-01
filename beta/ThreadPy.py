import threading
from time import sleep

def thread1():
    for i in range(5):
        sleep(1)
        print "T1 ",

def thread2():
    for i in range(5):
        sleep(2)
        print "T2 ",

def mainThread():
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()

if __name__=='__main__':
    mainThread()