# Nombre : Chullunquía Rosas, Sharon

import matplotlib.pyplot as plt
import math
import random

######## QUICKSORT #########

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    global count
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            count+=1
            i += 1
            y = A[i]
            A[i] = A[j]
            A[j] = y
    z = A[i+1]
    A[i+1] = A[r]
    A[r] = z
    return i+1

##################################

def promedio(A):
    sum=0
    for i in range (len(A)):
        sum=sum+A[i]
    prom = sum/len(A)
    return prom

def aleatorio(tamanio):
    return [random.randint(0, tamanio) for x in range(tamanio)]


###### MAIN ######

tamanios = []
for i in range (8,21):
    tam=2**i
    tamanios.append(tam)

contador = []
logaritmo = []

for i in range (len(tamanios)):
    results = []
    logaritmo.append(tamanios[i]*(math.log(tamanios[i],2)))
    for j in range (201):
        A= aleatorio(tamanios[i])
        count=0
        quicksort(A,0,len(A)-1)
        results.append(count)
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
####### COMPARACION DE PROMEDIO y n * lg(n) #######

fig2, ax2 = plt.subplots()
ax2.plot(tamanios, logaritmo, label='QuickSort con logaritmo') # 1 + ln(n)
ax2.plot(tamanios, contador, label='QuickSort con contador')  # promedio
ax2.set_xlabel('Tamaños de los arreglos')  # Add an x-label to the axes.
ax2.set_ylabel('Tiempo promedio')  # Add a y-label to the axes.
ax2.set_title("Promedio de veces que la línea 4 es ejecutada en Maximo")
ax2.legend()
ax2.grid()
fig2.savefig("Tiempos_promedio.png")
