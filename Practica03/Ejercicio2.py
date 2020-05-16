# Nombre : Chullunquía Rosas, Sharon

import matplotlib.pyplot as plt
import random
import time

############# MERGE SORT (TOP-DOWN) #############

def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

############# MERGE SORT (INTERCALACION) #############

def INTERCALA(A, p, q, r):
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


def MERGE_SORT(A,p,r):
    if p < r -1:
        q = (p+r)//2
        MERGE_SORT(A,p,q)
        MERGE_SORT(A,q,r)
        INTERCALA(A,p,q,r)
##############################################
def mostrar(A):
    for i in range (len(A)):
        print(A[i])

def creciente(tamanio):
    return [x for x in range(1, tamanio+1)]

def decreciente(tamanio):
    return [x for x in range(tamanio, 0, -1)]

def aleatorio(tamanio):
    return [random.randint(0, tamanio) for x in range(tamanio)]


def generador(elec,tamanio):
    array=[]
    if elec == "creciente":
        array=creciente(tamanio)
        return array
    elif elec == "decreciente":
        array=decreciente(tamanio)
        return array
    elif elec == "aleatorio":
        array=aleatorio(tamanio)
        return array

###### MAIN ######

tamanios = [400,500,800,1000,1500,2000,2500,3000,4000,8000,9000]
print("*Creciente")
print("*Decreciente")
print("*Aleatorio")
elec=str(input("Escribe tu opcion :"))
#### MERGE SORT (TOP-DOWN) #######
tiemposReal = []
#### MERGE SORT (INTERCALACION) #######
tiemposReal2 = []

for i in range (len(tamanios)):
    A = generador(elec,tamanios[i])
    A_copy = A
    #### MERGE SORT (TOP-DOWN) #######
    start_time = time.time()
    merge_sort(A,0, len(A)-1)
    real_time = time.time() - start_time
    tiemposReal.append(real_time )##tiempo real
    #### MERGE SORT (INTERCALACION) #######
    start_time = time.time()
    MERGE_SORT( A_copy,0,len(A_copy) )
    real_time = time.time() - start_time
    tiemposReal2.append(real_time )##tiempo real

print('\n')
print("TIEMPO REAL:",'\n')
print("Merge sort (top-down) :",'\n')
mostrar(tiemposReal)
print('\n')
print("Merge sort (Intercalacion):",'\n')
mostrar(tiemposReal2)

# GRAFICA
#######Comparacion de tiempos reales######

fig2, ax2 = plt.subplots()
ax2.plot(tamanios, tiemposReal, label='Merge Sort top-down en tiempo real')
ax2.plot(tamanios, tiemposReal2, label='Merge Sort Intercalacion en tiempo real')
ax2.set_xlabel('Tamaños de los arreglos')  # Add an x-label to the axes.
ax2.set_ylabel('Tiempo real')  # Add a y-label to the axes.
ax2.set_title("Comparación de Merge Sort top-down e Intercala en arreglos tipo " + elec)
ax2.legend()
ax2.grid()
fig2.savefig(elec + "_tiempo_real.png")
