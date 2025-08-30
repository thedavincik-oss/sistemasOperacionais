#importação de bibliotecas
import threading 
import time
import math
#Estrutura da Thread
def estruturaThread(nome, inicio, fim):
    for i in range(inicio, fim +1):
        print(f"{nome} -> {i}")
        time.sleep(1)

thread1 = threading.Thread(target=estruturaThread, args=("thread1",1, 10))
thread2 = threading.Thread(target=estruturaThread, args=("thread2",11, 20))

thread1.start()
thread2.start()