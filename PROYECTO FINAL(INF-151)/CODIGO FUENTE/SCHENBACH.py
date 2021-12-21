import numpy as np
from matplotlib import pyplot as plt
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