import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
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
