# Nombre : Chullunquía Rosas, Sharon

import matplotlib.pyplot as plt
import random
import time

########## QUICKSORT ##########

def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def Quick_Sort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		Quick_Sort(arr, low, pi-1) 
		Quick_Sort(arr, pi+1, high) 

# Driver code to test above 
# arr = [10, 7, 8, 9, 1, 5] 
# n = len(arr) 
# quickSort(arr,0,n-1) 
# print(arr)


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
for i in range (1000,105001,1000):
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
