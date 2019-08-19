# -*- coding: utf-8 -*-
"""

@author: Manuel
"""
#Lenguaje de la F

try:
    oracion= input("introduzca una cadena ")
    oracion=oracion.replace("a", "afa")
    oracion=oracion.replace("e", "efe")
    oracion=oracion.replace("i", "ifi")
    oracion=oracion.replace("o", "ofo")
    oracion=oracion.replace("u", "ufu")
    oracion=oracion.replace("á", "áfa")
    oracion=oracion.replace("é", "éfe")
    oracion=oracion.replace("í", "ífi")
    oracion=oracion.replace("ó", "ófo")
    oracion=oracion.replace("ú", "úfu")
    oracion=oracion.replace("y", "yfi")
    
    print("resultado: "+oracion)
       
except ValueError:
    print("el valor no fue cadenas")
