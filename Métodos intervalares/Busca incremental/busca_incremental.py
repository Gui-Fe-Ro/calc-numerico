#Matéria: Cálculo numérico
#Aluno: Guilherme Félix Rosa

#imports
import numpy as np
from math import e, cos

#Variáveis
intervaloA = 0
intervaloB = 3
qtdSubIntervalos = 100

#Algoritmo
tamSubintervalos = ((intervaloB-intervaloA)/100)

subintervalos = []
subintervalos = np.zeros(qtdSubIntervalos)

#Determinando o tamnho dos subintervalos 
for i in range(len(subintervalos)):
    if(i==0):
        subintervalos[i] = 0
    else:
        subintervalos[i] = subintervalos[i-1]+tamSubintervalos
    
#Verificando a raíz
fx = 0
fxAux = 0
intervalos = np.zeros(2)
intervalos[0] = 0
intervalos[1] = 0 

for i in range(len(subintervalos)):
    #Fórmula
    if(i==0):
        fxAux = (e**subintervalos[i])-4+((7/2)*(cos(2*subintervalos[i])))
    else:
        fx = (e**subintervalos[i])-4+((7/2)*(cos(2*subintervalos[i])))
        
        #Verificando a mudança de sinal
        if(fxAux<0):
            if(fx>0):
                intervalos[0] = subintervalos[i-1]
                intervalos[1] = subintervalos[i]
                print(f'Intervalos: [{intervalos[0]},{intervalos[1]}]')
        if(fxAux>0):
            if(fx<0):
                intervalos[0] = subintervalos[i-1]
                intervalos[1] = subintervalos[i]
                print(f'Intervalos: [{intervalos[0]},{intervalos[1]}]')
        
        fxAux = fx