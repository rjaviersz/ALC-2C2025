# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 21:45:02 2025

@author: rjavi
"""
import numpy as np

# Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64
def error(x,y):
    x = np.float64(x)
    y = np.float64(y)
    return abs(y-x)
    


# # Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float64
# def error relativo(x,y):


# # Devuelve True si ambas matrices son iguales y False en otro caso.
# def matricesIguales(A,B):


def sonIguales(x,y,atol=1e-08):
    return np.allclose(error(x,y),0,atol=atol)
 
assert(not sonIguales(1,1.1))
assert(sonIguales(1,1 + np.finfo('float64').eps))
assert(not sonIguales(1,1 + np.finfo('float32').eps))
assert(not sonIguales(np.float16(1),np.float16(1) + np.finfo('float32').eps))
assert(sonIguales(np.float16(1),np.float16(1) + np.finfo('float16').eps,atol=1e-3))









