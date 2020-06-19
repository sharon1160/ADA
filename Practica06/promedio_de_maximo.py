# Nombre : Chullunquía Rosas, Sharon

import matplotlib.pyplot as plt
import math
import random

############ MAXIMO ###########

def maximo(A):
    count=0
    max=A[0]
    for i in range (1,len(A)):
        if A[i] > max :
            max = A[i]
            count+=1
    return count


####################################

def promedio(A):
    sum=0
    for i in range (len(A)):
        sum=sum+A[i]
    prom = sum/len(A)
    return prom

def aleatorio(tamanio):
    return [random.randint(0, tamanio) for x in range(tamanio)]


######### MAIN #########

tamanios = []
for i in range (8,21):
    tam=2**i
    tamanios.append(tam)

contador = []
logaritmo = []

for i in range (len(tamanios)):
    results = []
    logaritmo.append(math.log(tamanios[i])+1)
    for j in range (200):
        A= aleatorio(tamanios[i])
        results.append(maximo(A))
    contador.append(promedio(results))


##### TAMAÑOS #######
print("TAMANIOS DE LAS LISTAS ")
print(tamanios)

##### PROMEDIOS CON CONTADOR #######    
#print("Promedio de los 2 arreglos de cada tamanio \n")
print("PROMEDIOS DE EJECUCION DE LA LINEA 4 CON CONTADOR")
print(contador)
##### PROMEDIOS CON LOGARITMO #######    
print("PROMEDIOS DE EJECUCION DE LA LINEA 4 CON LOGARITMO)")
print(logaritmo)


# GRAFICA
#######Comparacion de tiempos reales######

fig2, ax2 = plt.subplots()
ax2.plot(tamanios, logaritmo, label='Maximo con logaritmo')
ax2.plot(tamanios, contador, label='Maximo con contador')
ax2.set_xlabel('Tamaños de los arreglos')  # Add an x-label to the axes.
ax2.set_ylabel('Tiempo promedio')  # Add a y-label to the axes.
ax2.set_title("Promedio de veces que la línea 4 es ejecutada en Maximo")
ax2.legend()
ax2.grid()
fig2.savefig("Tiempos_promedio.png")
