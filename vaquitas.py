import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

sem = threading.Semaphore(1) # semaforo pra que vallan de a 1

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "v")

  def run(self):
    while(True):
      self.avanzar()

vacas = []
for i in range(5): #las vacas se deben detener en 10 y pasar de a 1 hata la posicion 30 , ahi larga a 
  v = Vaca()       # la otra vaca que agarro el acquire
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
