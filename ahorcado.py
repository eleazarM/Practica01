# -*- coding: utf-8 -*-
"""


@author: Manuel
"""
#programa de ahorcado

from random import randint

class ahorcado:
   
    #e=0
    mostrar=[]
    correcto=0
    
    def __init__(self,p,E,):
       self.p = p
       self.E = E
       for i in range(0,len(self.p)): #se genera una cadena del mismo tamaño de la palabra para mostrar la palabra oculta
           self.mostrar.append('_')           
    
    def jugar(self,c): 
        aux=0 # valor para no perder el indice de la cadena original
        respuesta=1  #valor para saber si se encontro el caracter en la palabra -1 es que no
        longitud=len(self.p)
        auxiliar=self.p
        respuesta= auxiliar.find(c)
        if(respuesta < 0): # si no se encuentra la letra se cuenta como error
            self.E = self.E - 1
        while(respuesta>=0):# se realiza un ciclo por si se encuentra más de una vez la letra
            respuesta= auxiliar.find(c)
            if(respuesta>=0):
                auxiliar = auxiliar[0:respuesta]+auxiliar[respuesta+1:longitud]
                if(self.mostrar[aux+respuesta]=='_'):
                    self.correcto=self.correcto+1
                self.mostrar[aux+respuesta]=c 
                aux=aux+1
        print(f"Intentos restantes: {self.E}")
        print(self.mostrar) 
        
palabras=[]

file = open('listado-general.txt','r', encoding="utf8")
for line in file:
    palabras.append(line)
file.close

valor= randint(3,7) #valor aleatorio para los errores posibles
palabra=palabras[randint(0,len(palabras))] # se selecciona una palabra alazar
palabra= palabra[0:len(palabra)-1] #para quitar el salto de línea
ahorcar=ahorcado(palabra,valor) #se inicializa la clase con la palabra a adivinar y la cantidad de errores posibles

#ciclo hasta que el error llegue a 0 o correcto sea del tamaño de la palabra
while((ahorcar.E > 0) and (ahorcar.correcto < len(palabra))): 
    c= input("introduzca una letra ")
    ahorcar.jugar(c)
if(ahorcar.E==0):
    print("perdiste")
else:
    print("ganaste")

