from youtube import DescargarVideo as DVL
from multiprocessing import Process


def procesarListaLink(lista):
    
    lista1 = list()
    lista2 = list()
    
    cantidad_links = len(lista)

    while cantidad_links != 0:
        if(cantidad_links % 2 == 0):
            lista2.append(lista[cantidad_links-1])
        else:
            lista1.append(lista[cantidad_links-1])
        cantidad_links -=1
    
    parent1 = Process(target=DVL,args=(lista1, ))
    parent2 = Process(target=DVL,args=(lista2, ))

    parent1.start()
    parent2.start()
    parent1.join()
    parent2.join()
    