import serial, time, threading, Queue

inQueue = Queue.Queue()
outQueue = Queue.Queue()

def inFunc():
	while True:
		print 'Left'
		time.sleep(5)

def outFunc():
	while True:
		print 'right'
		time.sleep(5)

outThread = threading.Thread(target=inFunc)
inThread = threading.Thread(target=outFunc)

inThread.start()
outThread.start()
inThread.join()
outThread.join()