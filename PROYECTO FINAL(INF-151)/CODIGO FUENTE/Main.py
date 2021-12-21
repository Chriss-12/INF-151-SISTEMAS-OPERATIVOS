from FIFO import FIFO
from PRIORIDADES import Prioridades
from RR import RoundRobin

from OPT import OPT
from FIFO1 import FIFO1
from LRU import LRU

from SCHENBACH import SCHENBACH
from FIFO2 import FIFO2
from SSTF import SSTF

"""
#1.	Administracion de procesos.
f1 = FIFO(Proc=['A', 'B', 'C', 'D', 'E', 'F'], Tini=[3, 1, 0, 6, 3, 9], Tcpu=[3, 2, 4, 2, 3, 1])
P1 = Prioridades(Proc=['A', 'B', 'C', 'D', 'E'], Tini=[7, 8, 8, 10, 12], Tcpu=[3, 4, 2, 3, 2], Prioridades=[3, 2, 1, 4, 5])
RR1 = RoundRobin(Proc=['A', 'B', 'C', 'D', 'E'], Tini=[0, 1, 3, 9, 12], Tcpu=[3, 5, 2, 5, 5], Quantum=10)
#2.	Administracion de memoria por paginación para el reemplazo de páginas.
O1 = OPT(Demanda=[2, 3, 4, 2, 1, 3, 5, 2, 4, 3, 2, 1], Marcos=3)
F11 = FIFO1(Demanda=[3, 2, 1, 4, 6, 5, 3, 2, 4, 3], Marcos=4)
L1 = LRU(Demanda=[2, 4, 6, 2, 3, 4, 5, 2, 1, 2, 3, 4], Marcos=3)
#3.	Administracion de memoria secundaria
S1 = SCHENBACH(Peticiones=[10, 15, 10, 30, 15, 10, 20, 30, 10, 40, 20, 30])
FF21 = FIFO2(Peticiones=[10, 40, 5, 20, 15, 35, 40, 5, 10, 25, 10, 35, 10, 5, 20], inicio=20)
SS1 = SSTF(Peticiones=[10, 40, 5, 20, 15, 35, 40, 5, 10, 25, 10, 35, 10, 5, 20], inicio=20)"""

"""f1.solucion(); P1.solucion(); RR1.solucion()

O1.solucion(); F11.solucion(); L1.solucion()

FF21.solucion(); S1.solucion(); SS1.solucion()"""

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