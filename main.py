import serial, time, threading, Queue

inQueue = Queue.Queue()
outQueue = Queue.Queue()

inSerial = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.001)
outSerial = serial.Serial('/dev/ttyUSB1', 9600, timeout=0.001)

inSerial.open()
outSerial.open()

def inFunc():
	while True:
		if not outQueue.empty():
			outFrame = outQueue.get_nowait()
			outSerial.write(outFrame)
		readFrame = inSerial.read()
		if readFrame:
			inQueue.put(readFrame)
		time.sleep(0.0001)

def outFunc():
	while True:
		if not inQueue.empty():
			inFrame = inQueue.get_nowait()
			inSerial.write(inFrame)
		readFrame = outSerial.read()
		if readFrame:
			outQueue.put(readFrame)
		time.sleep(0.0001)

outThread = threading.Thread(target=inFunc)
inThread = threading.Thread(target=outFunc)

inThread.start()
outThread.start()
inThread.join()
outThread.join()