import threading
import time

class Thread1(threading.Thread):
	def __init__(self, threadName):
		threading.Thread.__init__(self)
		self.threadName = threadName

	def run(self):
		print(self.threadName)
		for i in range(5):
			print(1)
			time.sleep(1)
		print("Finalizando %s" % (self.threadName))

class Thread2(threading.Thread):
	def __init__(self, threadName):
		threading.Thread.__init__(self)
		self.threadName = threadName

	def run(self):
		print(self.threadName)
		for i in range(5):
			print(2)
			time.sleep(1)
		print("Finalizando %s" % (self.threadName))

t1 = Thread1("Thread A")
t2 = Thread2("Thread B")

t1.start()
t2.start()

t1.join()
t2.join()

print("Terminando as Threads")
