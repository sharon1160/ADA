#Autor : Chullunquía Rosas, Sharon Rossely

import matplotlib.pyplot as plt
import random
import time

### LOS DOS ALGORITMOS QUE RETORNAN EL TIEMPO REAL ###

def insertion_sort(A):
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
      A[i+1] = A[i]
      i = i - 1
    A[i + 1] = key

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

###############################################################
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

def copiarTimes(A,B):#copiar A en B
    for i in range (len(A)):
        B.append(A[i])

def sumarTimes(A,B):#sumar A a B
    for i in range (len(A)):
        B[i]=B[i] + A[i]

def dividir(B):#divide cada elemento entre el numero de veces que se tomo el tiempo 
    for i in range (len(B)):#para así sacar el promedio en tiempo
        B[i]=B[i]/10


# MAIN
#tamanios = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#tamanios = [25, 50, 75, 100, 125, 150, 175,200]
tamanios = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
print("*Creciente")
print("*Decreciente")
print("*Aleatorio")
elec=str(input("Escribe tu opcion :"))
#### Promedio Merge Sort #######
PromedioTimeMerge = []
#### Promedio Insert Sort #######
PromedioTimeInsert = []
#### Merge Sort #######
tiemposReal = []
#### Insert Sort #######
tiemposReal2 = []

for j in range (10):#número de veces que se hara la medición de tiempo
    for i in range (len(tamanios)):
            #### Merge Sort #######
            start_time = time.time()
            merge_sort(generador(elec,tamanios[i]),0, len(generador(elec,tamanios[i]))-1)
            real_time = time.time() - start_time
            tiemposReal.append(real_time )##tiempo real
            #### Insert Sort #######
            start_time = time.time()
            insertion_sort( generador(elec,tamanios[i]) )
            real_time = time.time() - start_time
            tiemposReal2.append(real_time )##tiempo real
    if j==0 :
        copiarTimes(tiemposReal,PromedioTimeMerge)#en la primera medición copiamos los elementos  
        copiarTimes(tiemposReal2,PromedioTimeInsert)#en un array donde calcularemos el promedio
    elif j!=0:                                      
        sumarTimes(tiemposReal,PromedioTimeMerge)#a partir de la segunda medición empezamos a sumar 
        sumarTimes(tiemposReal2,PromedioTimeInsert)# los tiempos
    tiemposReal = []#vaciamos los arreglos para que queden en cero ya que si no hacemos esto 
    tiemposReal2 = []#en el arreglo seguiría agregandose al final de todo lo agregado
dividir(PromedioTimeMerge)#finalmente se divide cada elemento
dividir(PromedioTimeInsert)#para obtener el promedio

print('\n')
print("TIEMPOS PROMEDIOS EN TIEMPO REAL:",'\n')
print("Merge sort:",'\n')
mostrar(PromedioTimeMerge)
print("Insert sort:",'\n')
mostrar(PromedioTimeInsert)

# GRAFICA
#######Comparacion de tiempos reales######

fig2, ax2 = plt.subplots()
ax2.plot(tamanios, PromedioTimeInsert, label='Inserción en tiempo promedio real')
ax2.plot(tamanios, PromedioTimeMerge, label='Merge en tiempo promedio real')
ax2.set_xlabel('Tamaños de los arreglos')  # Add an x-label to the axes.
ax2.set_ylabel('Tiempo promedio real')  # Add a y-label to the axes.
ax2.set_title("Comparación de Merge e Insert Sort en arreglos tipo " + elec)
ax2.legend()
ax2.grid()
fig2.savefig(elec + "_tiempo_promedio_real.png")


