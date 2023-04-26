#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

def banquero(n_procesos, n_recursos, maximo, asignado, disponible,verbose):
    """
    Implementación del algoritmo del banquero.
    
    Args:
    n_processes (int): número de procesos en el sistema.
    n_resources (int): número de recursos en el sistema.
    maximo (np.array): matriz que representa el número máximo de recursos que cada proceso puede solicitar.
    asignado (np.array): matriz que representa la cantidad de recursos que actualmente se le han asignado a cada proceso.
    disponible (np.array): vector que indica la cantidad de recursos disponibles en el sistema.
    verbose (bool): elegir si se quiere imprimir verbose
    
    Returns:
    tuple: un booleano que indica si el sistema es seguro o no, 
    una lista que contiene el orden en que los procesos pueden ejecutarse de manera segura 
    y una lista que contiene la secuencia de ejecución de los procesos.
"""
    # inicialización
    terminado = np.zeros(n_procesos, dtype=bool) #Inicializando en 0 las matrices; False = no finaliza el proceso
    necesidad = maximo - asignado #resta entre las matrices por lo que nos da la matriz de necesidades
    orden = []
    secuencia = []
    
    # ciclo principal
    if verbose:
        print("Recursos disponibles",disponible)
        
    while len(orden) < n_procesos:
        seguro = False
    
        for i in range(n_procesos):
            if not terminado[i] and np.all(disponible >= necesidad[i]):
                
                disponible += asignado[i]
                terminado[i] = True
                seguro = True
                orden.append(i)
                secuencia.append('P' + str(i))
                if verbose:
                    print("\tP",i," necesita",necesidad[i])
                    print("\tP",i," terminó")
                    print("Recursos disponibles",disponible)
        
        if not seguro:
            if verbose:
                print("Los recursos disponibles no satisfacen a los procesos:")
                for i in range(n_procesos):
                    if not terminado[i]:
                        print("\tP",i,"necesita",necesidad[i])
                    
            break
        
    seguro = len(orden) == n_procesos
    
    if seguro:
        print("Es seguro asignar los recursos.")
        print("Orden de ejecución de los procesos:", orden)
        print("Secuencia de ejecución de los procesos:", " -> ".join(secuencia))
    else:
        print("No es seguro asignar los recursos.")
    
    return seguro, orden, secuencia


if __name__ == "__main__":  
    
    #entradas
    n_procesos = 7
    n_recursos = 5
    
    
    # matriz que representa el numero maximo de recursos que cada proceso puede solicitar
    maximo = np.array([[6, 4, 5, 7, 6], [2, 1, 1, 2, 1], [3, 2, 6, 2, 3], [5, 6, 4, 3, 5], [6, 5, 4, 6, 3], [3, 4, 6, 4, 4], [4, 3, 3, 2, 3]])
    # matriz que representa la cantidad de recursos que actualmente se le han asignado a cada proceso
    asignado = np.array([[0, 1, 0, 1, 1], [1, 0, 0,0, 1], [3, 0, 2, 1, 0], [0, 1, 1, 0, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 2, 1, 1, 0]])
    
    # vector que indica la cantidad de recursos disponibles en el sistema
    disponible = np.array([6, 6, 6, 6, 6]) #recursos minimos necesarios del ejemplo

    # ejecución del algoritmo del banquero
    banquero(n_procesos, n_recursos, maximo, asignado, disponible,True)
    
    print("\n\n\tPara una configuración diferente:\n")
    disponible2 = np.array([6, 5, 5, 5, 5]) #recursos minimos necesarios del ejemplo

    banquero(n_procesos, n_recursos, maximo, asignado, disponible2,True)
    
    print("\n\n\tPara una configuración no segura:\n")
    disponible2 = np.array([6, 5, 2, 3, 2]) #recursos minimos necesarios del ejemplo

    banquero(n_procesos, n_recursos, maximo, asignado, disponible2,True)
    
