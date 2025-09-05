# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


# =============================================================================
# En un archivo librerias.py, generar la siguiente lista de funciones. Preparar
#  para cada ejercicio un test que verifique que la operacion se esta realizando
#  correctamente. 
# =============================================================================

# =============================================================================
#   De la libraria numpy de Python, solo estan permitidos utilizar
# las funciones que convierten listas a arrays, las que devuelven el tamaño 
# de un array y las funciones que encuentran maximos o minimos.
# =============================================================================


import numpy as np 
import numpy.linalg as lng

# Ejercicio 1. Desarrollar una funcion esCuadrada(A) que devuelva verdadero
#  si la matriz A es cuadrada y Falso en caso contrario.

def esCuadrada(A):
    return len(A)== len(A[0]) # si nro Filas es igual a nro Columnas

def esCuadrada1(A):
    tamaño = A.shape 
    if (tamaño[0]==tamaño[1]):
        return True
    else:
        return False
    
A = np.random.randint(0,10,(2,2))
esCuadrada(A)
B = np.random.randint(0,10,(2,3))
esCuadrada(B)


# Ejercicio 2. Desarrollar una funcion triangSup(A) que devuelva la matriz U
# correspondiente a la matriz Triangular Superior de A sin su diagonal.

def triangSup(A):
    tamaño = A.shape 
    j = 1
    for filas in A:
        i = 0
        while i < j:
            filas[i] = 0
            i = i+1
        j = j + 1
    return A 

C = np.random.randint(0,10,(4,4))
print("C:", C, "\n","C triangulada:",triangSup(C.copy()))


            
            
            
            
            
            
    


    
















    