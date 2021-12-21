import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
#funciona
class FIFO:
    def graficar(self):
        x = np.array(self.TiempoInicial)
        y = np.array(self.TiempoFinal)
        plt.plot(x, y, 'og--', mfc = 'y', mec = 'y')
        plt.title('FIFO')
        plt.xlabel('Tiempo inicial')
        plt.ylabel('Tiempo final')
        plt.show()
        #plt.show()#para mostrar pero se queda esperando hasta cerrar la ventana
    def __init__(self, Proc, Tini, Tcpu):
        self.Proceso = Proc
        self.TiempoInicial = Tini
        self.TiempoCpu = Tcpu
        self.T = []; self.E = []; self.I = []; self.TiempoFinal = []
        self.contador = 0
        self.numeroProcesos = len(self.Proceso)
    def mostrar(self):
        nombres = ['Proceso', 'Tini', 'Tcpu', 'Tfin', 'T', 'E', 'I']
        dataFrame = pd.DataFrame(list(zip(self.Proceso, self.TiempoInicial, self.TiempoCpu,
                                          self.TiempoFinal, self.T, self.E, self.I)), columns=nombres)
        print(dataFrame)
        print(f'T = {round(sum(self.T) / self.numeroProcesos, 2)}\n'
              f'E = {round(sum(self.E) / self.numeroProcesos, 2)}\n'
              f'I = {round(sum(self.I) / self.numeroProcesos, 2)}')
    def calcularT(self):
        for i in range(self.numeroProcesos):
            self.T.append(self.TiempoFinal[i] - self.TiempoInicial[i])
    def calcularE(self):
        for i in range(self.numeroProcesos):
            self.E.append(self.T[i] - self.TiempoCpu[i])
    def calcularI(self):
        for i in range(self.numeroProcesos):
            self.I.append(round(self.TiempoCpu[i] / self.T[i], 2))
    def ordenar(self):
        #ordena Tini, Tcpu y Proc para poder hacer el FIFO
        for i in range(self.numeroProcesos):
            for j in range(self.numeroProcesos - 1):
                if self.TiempoInicial[j] > self.TiempoInicial[j + 1]:
                    self.TiempoInicial[j], self.TiempoInicial[j + 1] = self.TiempoInicial[j + 1], self.TiempoInicial[j]
                    self.Proceso[j], self.Proceso[j + 1] = self.Proceso[j + 1], self.Proceso[j]
                    self.TiempoCpu[j], self.TiempoCpu[j + 1] = self.TiempoCpu[j + 1], self.TiempoCpu[j]

    def calcularTfin(self):
        aux = 0
        for i in range(self.numeroProcesos):
            if i == 0:#inicialmente obtendra el valor aux
                aux = self.TiempoInicial[i] + self.TiempoCpu[i]
            else:
                aux += self.TiempoCpu[i]
            self.TiempoFinal.append(aux)

    def solucion(self):
        try:
            self.ordenar()
            self.calcularTfin()
            self.calcularT()
            """print(self.Proceso)
            print(self.TiempoInicial)
            print(self.TiempoCpu)
            print(self.TiempoFinal)"""
            self.calcularE()
            self.calcularI()
            self.mostrar()
            self.graficar()
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""f1 = FIFO(Proc=['A', 'B', 'C', 'D', 'E', 'F'], Tini=[3, 1, 0, 6, 3, 9], Tcpu=[3, 2, 4, 2, 3, 1])
f1.solucion()"""
# funciona
class FIFO1:  # PARA REEMPLAZO DE PAGINAS
    def __init__(self, Demanda, Marcos):
        self.Demanda = Demanda
        self.Marcos = Marcos
        self.Pila = []  # trabaja como memoria
        self.Falla = []
        self.numeroFallos = 0
        self.n = len(self.Demanda)
        self.contadorFifo = 0

    def PilaVacia(self):
        if len(self.Pila) == 0:
            return True
        return False

    def PilaLlena(self):
        if len(self.Pila) == self.Marcos:
            return True
        return False

    def Asignacion(self, x, contador):
        self.Pila[contador] = x
        self.contadorFifo += 1

    def FIFO(self):
        for x in self.Demanda:
            if self.PilaVacia() or (not self.PilaLlena() and not x in self.Pila):
                self.Pila.append(x)
                self.numeroFallos += 1
                self.Falla.append('x')
            elif self.PilaLlena():
                if x in self.Pila:
                    # si se encuentra x en la memoria se mantiene
                    self.Falla.append('-')
                else:
                    # aqui se usa FIFO porque no encuentra una referencia lejana
                    if not self.contadorFifo < self.Marcos:
                        self.contadorFifo = 0
                    self.Asignacion(x, self.contadorFifo)
                    self.Falla.append('x')
                    self.numeroFallos += 1

    def mostrarFallas(self):
        print('**********************FIFO****************************')
        print('D', *self.Demanda, '\n'
                                  ' ', *self.Falla, sep='  ')
        print(f'NFallos = {self.numeroFallos}\n'
              f'NBienes = {self.n - self.numeroFallos}'
              f'\n')

    def solucion(self):
        try:
            self.FIFO()
            self.mostrarFallas()
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")


"""O2 = FIFO1(Demanda=[3, 2, 1, 4, 6, 5, 3, 2, 4, 3], Marcos=4)
O2.solucion()
"""
class FIFO2:
    def __init__(self, Peticiones, inicio):
        self.Pistas = []
        self.Peticiones = Peticiones
        self.Movimientos = 0
        self.inicio = inicio

    def graficar(self):
        self.Peticiones.insert(0, self.inicio)
        y = np.array(self.Peticiones)
        x = np.array([i for i in range(1, len(self.Peticiones) + 1)])
        plt.plot(x, y, 'og--', mfc='y', mec='y')
        plt.title('FIFO')
        plt.xlabel('Peticiones')
        plt.ylabel('Pistas')
        plt.show()

    def FIFO(self):
        for x in range(len(self.Peticiones)):
            if x == 0:
                self.Movimientos += abs(self.Peticiones[x] - self.inicio)
            else:
                self.Movimientos += abs(self.Peticiones[x] - self.Peticiones[x - 1])

    def solucion(self):
        try:
            self.FIFO()
            print('**********************FIFO****************************')
            print(f'numero de movimientos = {self.Movimientos}')
            self.graficar()
        except Exception:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""FF21 = FIFO2(Peticiones=[10, 40, 5, 20, 15, 35, 40, 5, 10, 25, 10, 35, 10, 5, 20], inicio=20)
FF21.solucion()"""
#funciona
class LRU:
    def __init__(self, Demanda, Marcos):
        self.Demanda = Demanda
        self.Marcos = Marcos
        self.PilaMemoria = []#la memoria
        self.Pila = []#la pila que servira para hacer el reemplazo
        self.Falla = []
        self.numeroFallos = 0
        self.n = len(self.Demanda)
        self.contadorFifo = 0

    def PilaVacia(self, Pila):
        if len(Pila) == 0:
            return True
        return False

    def PilaLlena(self, Pila):
        if len(Pila) == self.Marcos:
            return True
        return False

    def PilaSubirElemento(self, x):
        elem = self.Pila.pop(self.Pila.index(x))
        self.Pila.append(elem)

    def PilaApilarElemento(self, x):
        reemplazar = self.Pila.pop(0)
        self.Pila.append(x)
        self.PilaMemoria[self.PilaMemoria.index(reemplazar)] = x

    def LRU(self):
        for x in self.Demanda:
            if self.PilaVacia(self.PilaMemoria) or (not self.PilaLlena(self.PilaMemoria)):
                self.PilaMemoria.append(x)
                self.Pila.append(x)
                self.Falla.append('x')
                self.numeroFallos += 1
            else:
                if x in self.PilaMemoria:
                    self.Falla.append('-')
                    self.PilaSubirElemento(x)
                else:
                    self.PilaApilarElemento(x)
                    self.Falla.append('x')
                    self.numeroFallos += 1

    def mostrarFallas(self):
        print('**********************LRU****************************')
        print('D',*self.Demanda, '\n'
                                 ' ',*self.Falla, sep='  ')
        print(f'NFallos = {self.numeroFallos}\n'
              f'NBienes = {self.n - self.numeroFallos}'
              f'\n')

    def solucion(self):
        try:
           self.LRU()
           self.mostrarFallas()
           print(self.PilaMemoria)
           print(self.Pila)
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""L1 = LRU(Demanda=[2, 4, 6, 2, 3, 4, 5, 2, 1, 2, 3, 4], Marcos=3)
L1.solucion()"""
#funciona
class OPT:
    def __init__(self, Demanda, Marcos):
        self.Demanda = Demanda
        self.Marcos = Marcos
        self.Pila = []#trabaja como memoria
        self.Falla = []
        self.numeroFallos = 0
        self.n = len(self.Demanda)
        self.contadorFifo = 0
        self.anteriorSwFifo = 0

    def PilaVacia(self):
        if len(self.Pila) == 0:
            return True
        return False

    def PilaLlena(self):
        if len(self.Pila) == self.Marcos:
            return True
        return False

    def buscarReferenciaLejana(self, Di, x):
        posicion = -1; c = 0; posPila = 0
        for i in self.Pila:
            if (Di + 1 < self.n) and (i in self.Demanda[Di + 1: ]):
                if posicion == -1:
                    posicion = self.Demanda[Di + 1:].index(i)
                    posPila = c
                else:
                    cand = self.Demanda[Di + 1:].index(i)
                    if cand > posicion:
                        posicion = cand
                        posPila = c
            c += 1
        if posicion != -1:
            self.Pila[posPila] = x
            return True
        return False

    def FIFO(self, x, contador):
        if self.PilaVacia() or (not self.PilaLlena()):
            self.Pila.append(x)
        elif self.PilaLlena():
            self.Pila[contador] = x


    def OPT(self):
        Di = 0
        for x in self.Demanda:
            if self.PilaVacia() or (not self.PilaLlena() and not x in self.Pila):
                self.Pila.append(x)
                self.numeroFallos += 1
                self.Falla.append('x')
            elif self.PilaLlena():
                if x in self.Pila:
                    #si se encuentra x en la memoria + 1
                    self.Falla.append('-')
                else:
                    if self.buscarReferenciaLejana(Di, x):
                        # suponemos de que existe la referencia mas lejana aqui se hace uso
                        # del OPT
                        self.numeroFallos += 1
                        self.Falla.append('x')
                        self.anteriorSwFifo = 1
                    else:
                        # aqui se usa FIFO porque no encuentra una referencia lejana
                        if self.anteriorSwFifo:
                            self.contadorFifo = 0
                        else:
                            if self.contadorFifo + 1 < self.Marcos:
                                self.contadorFifo += 1
                            else:
                                self.contadorFifo = 0
                        self.FIFO(x, self.contadorFifo)
                        self.Falla.append('x')
                        self.numeroFallos += 1
                        self.anteriorSwFifo = 0
            Di += 1

    def mostrarFallas(self):
        print('**********************OPT****************************')
        print('D',*self.Demanda, '\n'
                                 ' ',*self.Falla, sep='  ')
        print(f'NFallos = {self.numeroFallos}\n'
              f'NBienes = {self.n - self.numeroFallos}'
              f'\n')

    def solucion(self):
        try:
           self.OPT()
           self.mostrarFallas()
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""D = [2, 3, 4, 2, 1, 3, 5, 2, 4, 3, 2, 1]
O1 = OPT(Demanda=D, Marcos=3)
O1.solucion()
D1 = [3, 2, 1, 4, 6, 5, 3, 2, 4, 3]
O2 = OPT(Demanda=D1, Marcos=4)
O2.solucion()"""
#Funciona
class Prioridades:
    def graficar(self):
        x = np.array(self.TiempoInicial)
        y = np.array(self.TiempoFinal)
        plt.plot(x, y, 'og--', mfc = 'y', mec = 'y')
        plt.title('PRIORIDADES(PR)')
        plt.xlabel('Tiempo inicial')
        plt.ylabel('Tiempo final')
        plt.show()
        #plt.show()#para mostrar pero se queda esperando hasta cerrar la ventana
    def __init__(self, Proc, Tini, Tcpu, Prioridades):
        self.Proceso = Proc
        self.TiempoInicial = Tini
        self.TiempoCpu = Tcpu
        self.T = []; self.E = []; self.I = []; self.TiempoFinal = []; self.Prioridades = Prioridades
        self.contador = 0
        self.numeroProcesos = len(self.Proceso)
    def mostrar(self):
        print('**********************Prioridades****************************')
        nombres = ['Proceso', 'Tini', 'Tcpu', 'Prio', 'Tfin', 'T', 'E', 'I']
        dataFrame = pd.DataFrame(list(zip(self.Proceso, self.TiempoInicial, self.TiempoCpu, self.Prioridades,
                                          self.TiempoFinal, self.T, self.E, self.I)), columns=nombres)
        print(dataFrame)

        print(f'T = {round(sum(self.T) / self.numeroProcesos, 2)}\n'
              f'E = {round(sum(self.E) / self.numeroProcesos, 2)}\n'
              f'I = {round(sum(self.I) / self.numeroProcesos, 2)}\n')
    def calcularT(self):
        for i in range(self.numeroProcesos):
            self.T.append(self.TiempoFinal[i] - self.TiempoInicial[i])
    def calcularE(self):
        for i in range(self.numeroProcesos):
            self.E.append(self.T[i] - self.TiempoCpu[i])
    def calcularI(self):
        for i in range(self.numeroProcesos):
            self.I.append(round(self.TiempoCpu[i] / self.T[i], 2))
    def ordenar(self):
        #ordena Tini, Tcpu y Proc para poder hacer el FIFO
        for i in range(self.numeroProcesos):
            for j in range(self.numeroProcesos - 1):
                if self.TiempoInicial[j] > self.TiempoInicial[j + 1]:
                    self.TiempoInicial[j], self.TiempoInicial[j + 1] = self.TiempoInicial[j + 1], self.TiempoInicial[j]
                    self.Proceso[j], self.Proceso[j + 1] = self.Proceso[j + 1], self.Proceso[j]
                    self.TiempoCpu[j], self.TiempoCpu[j + 1] = self.TiempoCpu[j + 1], self.TiempoCpu[j]
                elif self.TiempoInicial[j] == self.TiempoInicial[j + 1] and self.Prioridades[j] > self.Prioridades[j + 1]:
                    self.TiempoInicial[j], self.TiempoInicial[j + 1] = self.TiempoInicial[j + 1], self.TiempoInicial[j]
                    self.Proceso[j], self.Proceso[j + 1] = self.Proceso[j + 1], self.Proceso[j]
                    self.TiempoCpu[j], self.TiempoCpu[j + 1] = self.TiempoCpu[j + 1], self.TiempoCpu[j]

    def calcularTfin(self):
        aux = 0
        for i in range(self.numeroProcesos):
            if i == 0:#inicialmente obtendra el valor aux
                aux = self.TiempoInicial[i] + self.TiempoCpu[i]
            else:
                aux += self.TiempoCpu[i]
            self.TiempoFinal.append(aux)

    def solucion(self):
        try:
            self.ordenar()
            self.calcularTfin()
            self.calcularT()
            self.calcularE()
            self.calcularI()
            self.mostrar()
            self.graficar()
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""
P1 = Prioridades(Proc=['A', 'B', 'C', 'D', 'E'], Tini=[7, 8, 8, 10, 12], Tcpu=[3, 4, 2, 3, 2], Prioridades=[3, 2, 1, 4, 5])
"""

#funciona
class RoundRobin:
    def __init__(self, Proc, Tini, Tcpu, Quantum):
        self.Proceso = Proc
        self.TiempoInicial = Tini
        self.TiempoCpu = Tcpu
        self.contador = 0
        self.numeroProcesos = len(self.Proceso)
        self.quantum = Quantum
        self.T = []; self.E = []; self.I = []; self.TiempoFinal = [0 for i in range(self.numeroProcesos)]
    def graficar(self):
        x = np.array(self.TiempoInicial)
        y = np.array(self.TiempoFinal)
        plt.plot(x, y, 'og--', mfc = 'y', mec = 'y')
        plt.title('Round Robin(RR)')
        plt.xlabel('Tiempo inicial')
        plt.ylabel('Tiempo final')
        plt.show()
    #plt.show()#para mostrar pero se queda esperando hasta cerrar la ventana
    def calcularT(self):
        for i in range(self.numeroProcesos):
            self.T.append(self.TiempoFinal[i] - self.TiempoInicial[i])
    def calcularE(self):
        for i in range(self.numeroProcesos):
            self.E.append(self.T[i] - self.TiempoCpu[i])
    def calcularI(self):
        for i in range(self.numeroProcesos):
            self.I.append(round(self.TiempoCpu[i] / self.T[i], 2))
    def ordenar(self):
        #ordena Tini, Tcpu y Proc para poder hacer el FIFO
        for i in range(self.numeroProcesos):
            for j in range(self.numeroProcesos - 1):
                if self.TiempoInicial[j] > self.TiempoInicial[j + 1]:
                    self.TiempoInicial[j], self.TiempoInicial[j + 1] = self.TiempoInicial[j + 1], self.TiempoInicial[j]
                    self.Proceso[j], self.Proceso[j + 1] = self.Proceso[j + 1], self.Proceso[j]
                    self.TiempoCpu[j], self.TiempoCpu[j + 1] = self.TiempoCpu[j + 1], self.TiempoCpu[j]
    def mostrar(self):
        print('**********************Round Robin****************************')
        nombres = ['Proceso', 'Tini', 'Tcpu', 'Tfin', 'T', 'E', 'I']
        dataFrame = pd.DataFrame(list(zip(self.Proceso, self.TiempoInicial, self.TiempoCpu,
                                          self.TiempoFinal, self.T, self.E, self.I)), columns=nombres)
        print(dataFrame)
        print(f'T = {round(sum(self.T) / self.numeroProcesos, 2)}\n'
              f'E = {round(sum(self.E) / self.numeroProcesos, 2)}\n'
              f'I = {round(sum(self.I) / self.numeroProcesos, 2)}\n')

    def calcularTfin(self):
        TiempoCpu = self.TiempoCpu.copy()
        tiempo = self.TiempoInicial[0]
        ronda = 0
        i = 0
        while sum(TiempoCpu) != 0:#controla la salida
            if i < self.numeroProcesos:
                if TiempoCpu[i] == 0:
                    i += 1
                elif self.TiempoInicial[i] > tiempo:
                    i = 0
                else:
                    if TiempoCpu[i] - self.quantum >= 0:
                        TiempoCpu[i] -= self.quantum
                        tiempo += self.quantum
                    elif TiempoCpu[i] < self.quantum and TiempoCpu[i] != 0:
                        tiempo += TiempoCpu[i]
                        TiempoCpu[i] = 0
                    if TiempoCpu[i] == 0:
                        self.TiempoFinal[i] = tiempo

                    i += 1
            else:
                ronda += 1
                i = 0

    def solucion(self):
        try:
            self.ordenar()
            self.calcularTfin()
            self.calcularT()
            """print(self.Proceso)
            print(self.TiempoInicial)
            print(self.TiempoCpu)
            print(self.TiempoFinal)"""
            self.calcularE()
            self.calcularI()
            self.mostrar()
            self.graficar()
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

#f1 = RoundRobin(Proc=['A', 'B', 'C', 'D', 'E'], Tini=[7, 8, 8, 10, 12], Tcpu=[3, 4, 2, 3, 2], Quantum = 1)
#f1.solucion()
#f2 = RoundRobin(Proc=['A', 'B', 'C', 'D', 'E'], Tini=[0, 1, 3, 9, 12], Tcpu=[3, 5, 2, 5, 5], Quantum=1)
#f2.solucion()

class SCHENBACH:
    def __init__(self, Peticiones):
        self.Pistas = []
        self.Peticiones = list(sorted(set(Peticiones)))
        self.Movimientos = 0

    def graficar(self):
        x = np.array([i for i in range(1, len(self.Peticiones) + 1)])
        y = np.array(self.Peticiones)
        plt.plot(x, y, 'og--', mfc='y', mec='y')
        plt.title('SCHENBACH')
        plt.xlabel('Peticiones')
        plt.ylabel('Pistas')
        plt.show()

    def Scheenbach(self):
        self.Movimientos += self.Peticiones[0]
        for i in range(len(self.Peticiones) - 1):
            self.Movimientos += abs(self.Peticiones[i] - self.Peticiones[i + 1])

    def solucion(self):
        try:
            self.Scheenbach()
            print('**********************SCHENBACH****************************')
            print(f'numero de movimientos = {self.Movimientos}')
            self.graficar()
        except Exception:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""S1 = SCHENBACH(Peticiones=[10, 15, 10, 30, 15, 10, 20, 30, 10, 40, 20, 30])
S1.solucion()"""
class SSTF:
    def __init__(self, Peticiones, inicio):
        self.Pistas = []
        self.Peticiones = Peticiones
        self.Movimientos = 0
        self.inicio = inicio

    def graficar(self):
        self.Peticiones.insert(0, self.inicio)
        y = np.array(self.Peticiones)
        x = np.array([i for i in range(1, len(self.Peticiones) + 1)])
        plt.plot(x, y, 'og--', mfc='y', mec='y')
        plt.title('SSTF(Shortes seek time fast first)')
        plt.xlabel('Peticiones')
        plt.ylabel('Pistas')
        plt.show()

    def ordenar(self):
        auxiliar = []
        auxiliar2 = []
        for x in self.Peticiones:
            if x <= self.inicio:
                auxiliar.append(x)
            else:
                auxiliar2.append(x)
        self.Peticiones.clear()
        self.Peticiones.extend(sorted(auxiliar)[::-1])
        self.Peticiones.extend(sorted(auxiliar2))

    def SSTF(self):
        self.ordenar()
        for x in range(len(self.Peticiones)):
            if x == 0:
                self.Movimientos += abs(self.Peticiones[x] - self.inicio)
            else:
                self.Movimientos += abs(self.Peticiones[x] - self.Peticiones[x - 1])

    def solucion(self):
        try:
            self.SSTF()
            print('**********************SSTF****************************')
            print(f'numero de movimientos = {self.Movimientos}')
            self.graficar()
        except Exception:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""S1 = SSTF(Peticiones=[10, 40, 5, 20, 15, 35, 40, 5, 10, 25, 10, 35, 10, 5, 20], inicio=20)
S1.solucion()"""
while True:
    print('#######################Bienvenido!#######################'
          '\ningrese alguna de las opciones, e ingrese 0 para salir'.upper() + '\n'
          'ADMINISTRACION DE PROCESOS:\n'
          '     1. FIFO\n'
          '     2. PRIORIDADES(PR)\n'
          '     3. ROUND ROBIN(RR)\n'
          'Administracion de memoria por paginación para el reemplazo de páginas:'.upper() + '\n'
          '     4. OPT(Optimo)\n'
          '     5. FIFO\n'
          '     6. LRU\n'
          'ADMINISTRACION DE MEMORIA SECUNDARIA:\n'
          '     7. SCHENBACH\n'
          '     8. FIFO\n'
          '     9. SSTF')
    opcion = int(input())
    if opcion == 0:
        print('GRACIAS HASTA LUEGO!!!')
        break
    elif 1 <= opcion <= 9:
        if 1 <= opcion <= 3:
            Tcpu = list(map(int, input('Ingrese el Tiempo cpu(Tcpu): ').split()))
            Tini = list(map(int, input('Ingrese el Tiempo inicial(Tini): ').split()))
            Proc = [chr(i) for i in range(65, 91)][0: len(Tcpu)]
            if opcion == 1:
                f1 = FIFO(Proc, Tini, Tcpu)
                f1.solucion()
            elif opcion == 2:
                Prio = list(map(int, input('Ingrese las prioridades(Prioridad): ').split()))
                p1 = Prioridades(Proc, Tini, Tcpu, Prio)
                p1.solucion()
            else:
                Quantum = int(input('Ingrese el quantum(Q): '))
                rr1 = RoundRobin(Proc, Tini, Tcpu, Quantum)
                rr1.solucion()
        elif 4 <= opcion <= 6:
            Demanda = list(map(int, input('Ingrese las demandas: ').split()))
            Marcos = list(map(int, input('Ingrese los marcos: ').split()))
            if opcion == 4:
                o1 = OPT(Demanda, Marcos)
                o1.solucion()
            elif opcion == 5:
                ff1 = FIFO1(Demanda, Marcos)
                ff1.solucion()
            else:
                l1 = LRU(Demanda, Marcos)
                l1.solucion()
        else:
            Peticiones = list(map(int, input('Ingrese las Peticiones: ').split()))
            if opcion == 7:
                s1 = SCHENBACH(Peticiones)
                s1.solucion()
            else:
                inicio = int(input('Ingrese el Inicio: '))
                if opcion == 8:
                    ff2 = FIFO2(Peticiones, inicio)
                    ff2.solucion()
                else:
                    ss1 = SSTF(Peticiones, inicio)
                    ss1.solucion()

    else:
        print('INGRESO UN NUMERO NO VALIDO, POR FAVOR VUELVA A INGRESAR!!!')