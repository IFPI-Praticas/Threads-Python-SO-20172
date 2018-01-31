import threading
import time

buffer = [1,2,3,4,5,6,7,8]
ponteiro = 0

lock = threading.Lock()

def somador(nomeThread, index):
	global ponteiro
	for i in range(2):
		lock.acquire()
		valor1 = buffer[ponteiro]
		print("%s: valor 1: %d" % (nomeThread, valor1))
		time.sleep(1)
		ponteiro += 1
		lock.release()

		lock.acquire()
		valor2 = buffer[ponteiro]
		print("%s: valor 2: %d" % (nomeThread, valor2))
		time.sleep(1)
		ponteiro += 1
		print("%s soma = %d" %(nomeThread, (valor1+valor2)))
		lock.release()
		
t = threading.Thread(target=somador, args=("Thread A",0))
t2 = threading.Thread(target=somador, args=("Thread B",1))

t.start()
t2.start()