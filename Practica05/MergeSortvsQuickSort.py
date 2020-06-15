# Nombre : Chullunquía Rosas, Sharon

import matplotlib.pyplot as plt
import random
import time

########## QUICKSORT ##########

def Quick_Sort(L, first, last):
    # definimos los índices y calculamos el pivote
    i = first
    j = last    
    pivote = (L[i] + L[j]) / 2
    # iteramos hasta que i no sea menor que j
    while i < j:
        # iteramos mientras que el valor de L[i] sea menor que pivote
        while L[i] < pivote:
            # Incrementamos el índice
            i+=1
        # iteramos mientras que el valor de L[j] sea mayor que pivote
        while L[j] > pivote:
            # decrementamos el índice
            j-=1
        # si i es menor o igual que j significa que los índices se han cruzado
        if i <= j:
            # creamos una variable temporal para guardar el valor de L[j]
            x = L[j]
            # intercambiamos los valores de L[j] y L[i]
            L[j] = L[i]
            L[i] = x
            # incrementamos y decrementamos i y j respectivamente
            i+=1
            j-=1
    # si first es menor que j mantenemos la recursividad
    if first < j:
        L = Quick_Sort(L, first, j)
    # si last es mayor que i mantenemos la recursividad
    if last > i:
        L = Quick_Sort(L, i, last)
    # devolvemos la lista ordenada
    return L

############ MERGESORT (INTERCALA) ###########

def Intercala(A, p, q, r):
    B = []  
    i = p 
    j = q  
    while i < q and j < r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    while i < q:
        B.append(A[i])  
        i += 1
    while j < r:
        B.append(A[j]) 
        j += 1

    j = 0  
    for i in range(p, r):
        A[i] = B[j]
        j += 1


def Merge_Sort(A,p,r):
    if p < r -1:
        q = (p+r)//2
        Merge_Sort(A,p,q)
        Merge_Sort(A,q,r)
        Intercala(A,p,q,r)

########## GENERADOR DE ARREGLOS ALEATORIOS ##########

def aleatorio(tamanio):
    return [random.randint(0, tamanio) for x in range(tamanio)]


########## MAIN ##########

tamanios = []
for i in range (1000,100001,1000):
    tamanios.append(i)


###### QUICK SORT ######
tiemposReal = []
#### MERGE SORT (INTERCALA) ####
tiemposReal2 = []

for i in range (len(tamanios)):
    A = aleatorio(tamanios[i])
    A_copy = A
    ###### QUICK SORT ######
    start_time = time.time()
    Quick_Sort(A,0, len(A)-1)
    real_time = time.time() - start_time
    tiemposReal.append(real_time )##tiempo real
    #### MERGE SORT (INTERCALACION) #######
    start_time = time.time()
    Merge_Sort( A_copy,0,len(A_copy) )
    real_time = time.time() - start_time
    tiemposReal2.append(real_time )##tiempo real

print('\n')
print("TIEMPOS REALES:",'\n')
print("Quick sort :",'\n')
print(tiemposReal)
print('\n')
print("Merge sort (Intercala):",'\n')
print(tiemposReal2)

# GRAFICA
#######Comparacion de tiempos reales######

fig2, ax2 = plt.subplots()
ax2.plot(tamanios, tiemposReal, label='Quick Sort en tiempo real')
ax2.plot(tamanios, tiemposReal2, label='Merge Sort (Intercala) en tiempo real')
ax2.set_xlabel('Tamaños de los arreglos')  # Add an x-label to the axes.
ax2.set_ylabel('Tiempo real')  # Add a y-label to the axes.
ax2.set_title("Comparación de Quick Sort y Merge Sort (Intercala) con arreglos aleatorios ")
ax2.legend()
ax2.grid()
fig2.savefig("Aleatorio_tiempo_real.png")
