#Andrea Elias 17048 
#Andres Quinto 18288
#Algoritmos y Estructura de Datos
#Fecha: 28/02/19
#Esta es una simulacion de la corrida de procesos en un sistema
#operativo, con la ayuda de simpy


import simpy
import random
import math

# Variables a modificar (algunas)
CapacidadRAM = 100 #Capacidad del la memoria RAM
NumeroProcesos = 200 # Cantidad de procesos a realizar
NumeroCPU = 2 #Numeros de CPU a utilizar
Interval = 10 # Intervalo de los procesos
InstruccionesCPU = 6  # Cuantas instrucciones realiza el CPU por unidad de tiempo
TiempoOperacionInOut = 1  # Tiempo de operacion I/O
TiemposDeProcesos = []  # Lista para almacenar tiempos
random.seed(15) 

#-----Clase que crea los componentes de un Sistema Operativo como lo son los CPU's y la RAM------#

class SistemaOperativo:

    def __init__(self, env):
        self.RAM = simpy.Container(env, init=CapacidadRAM, capacity=CapacidadRAM)
        self.CPU = simpy.Resource(env, capacity=NumeroCPU)

#-----Clase que nos ayudara a modelar como trabaja un proceso dentro de una computadora-----#
        
class Proceso:

    def __init__(self, id, no, env, sistema_operativo):
        # Atributos del proceso
        self.id = id
        self.no = no
        self.instrucciones = random.randint(1, 10)
        self.memoriaRequerida = random.randint(1, 10)
        self.env = env
        self.terminated = False
        self.sistema_operativo = sistema_operativo
        self.createdTime = 0
        self.finishedTime = 0
        self.totalTime = 0
        self.proceso = env.process(self.procesar(env, sistema_operativo))

