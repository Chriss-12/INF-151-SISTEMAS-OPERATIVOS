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