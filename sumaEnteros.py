# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#sumatoria hasta n
resultado=0
try:
    n= int(input("introduzca un valor para la sumatoria "))
    for i in range(n+1):
        resultado=resultado+i
    print(f"el resultado es: {resultado}")
except ValueError:
    print("el valor no fue entero")
