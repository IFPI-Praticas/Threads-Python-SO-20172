import threading
import time

def executar_1(nomeThread):
	for i in range(5):
		print(1)
		time.sleep(1)

def executar_2(nomeThread):
	for i in range(5):
		print(2)
		time.sleep(1)

t = threading.Thread(target=executar_1, args=("Thread A",))
t2 = threading.Thread(target=executar_2, args=("Thread B",))
t.start()
t2.start()

t.join()
t2.join()
print("Threads Finalizadas!")