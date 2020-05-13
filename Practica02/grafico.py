import matplotlib.pyplot as plt
import random
import time

### LOS DOS ALGORITMOS QUE RETORNAN EL TIEMPO EN UNIDADES  ###

def insertion_sort1(A):
  comparaciones = 0  # Comparaciones
  asignaciones = 0  # Asignaciones
  memoria = 0  # asignaciones de memoria
  for j in range(1, len(A)):
    asignaciones += 1  # por el numero de veces que se asigna "j"
    key = A[j]
    i = j - 1
    asignaciones += 2  # por la asignacion del "key" e "i"
    while i >= 0 and A[i] > key:
      comparaciones  += 1  # por cada comparacion del while
      A[i+1] = A[i]
      i = i - 1
      asignaciones += 2  # por las asignaciones del "A[i+1]"" e "i"
    A[i + 1] = key
    asignaciones += 1  # por la asignacion "A[i + 1]"
  comparaciones  += len(A) - 1  # comparaciones de "j" en el for
  asignaciones += 1  # por el fin del ciclo for
  memoria += 1  # por el range
  unidades_tiempo = 2 * comparaciones + 8 * asignaciones + 200 * memoria  + (50 + len(A) * 10)
  return unidades_tiempo

def bubble_sort1(A):
  comparaciones  = 0  # Comparaciones
  asignaciones = 0  # Asignaciones
  memoria  = 0  # Asignaciones de  memoria
  n = len(A)
  asignaciones += 1  # por "n"
  while True:
    swapped = False
    asignaciones += 1  # por el "swapped"
    for i in range(1, n):
      asignaciones += 1  # por cada asignacion de "i"
      if A[i-1] > A[i]:
        comparaciones  += 1
        A[i-1], A[i] = A[i], A[i-1]# dos asignaciones
        swapped = True
        asignaciones += 3  # por las tres anteriores asignaciones
    if not swapped:
      break
    comparaciones  += 1  # por el if not swapped
  memoria  += 1  # por el range
  unidades_tiempo = 2 * comparaciones  + 8 * asignaciones + 200 * memoria  + (50 + len(A) * 10)
  return unidades_tiempo

### LOS DOS ALGORITMOS QUE RETORNAN EL TIEMPO REAL ###

def insertion_sort2(A):
  start_time = time.time()
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
      A[i+1] = A[i]
      i = i - 1
    A[i + 1] = key
  real_time = time.time() - start_time
  return real_time

def bubble_sort2(A):
  start_time = time.time()
  n = len(A)
  while True:
    swapped = False
    for i in range(1, n):
      if A[i-1] > A[i]:
        A[i-1], A[i] = A[i], A[i-1]# dos asignaciones
        swapped = True
    if not swapped:
      break
  real_time = time.time() - start_time
  return real_time

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


# MAIN
#tamanios=[10,20,30]
tamanios = [500, 1000, 2000, 5000, 10000, 20000]
print("*Creciente")
print("*Decreciente")
print("*Aleatorio")
elec=str(input("Escribe tu opcion :"))
#### Bubble Sort #######
tiemposUnidad =[]
tiemposReal = []
#### Insert Sort #######
tiemposUnidad2 =[]
tiemposReal2 = []
for i in range (len(tamanios)):
    #### Bubble Sort #######
    tiemposUnidad.append(bubble_sort1(generador(elec,tamanios[i])))##unidades
    tiemposReal.append(bubble_sort2(generador(elec,tamanios[i])))##tiempo real
    #### Insert Sort #######
    tiemposUnidad2.append(insertion_sort1(generador(elec,tamanios[i])))##unidades
    tiemposReal2.append(insertion_sort2(generador(elec,tamanios[i])))##tiempo real
print('\n')
print("TIEMPOS EN TIEMPO REAL:",'\n')
print("Bubble sort:",'\n')
mostrar(tiemposReal)
print("Insert sort:",'\n')
mostrar(tiemposReal2)
print('\n')
print("TIEMPOS EN UNIDADES:",'\n')
print("Bubble sort:",'\n')
mostrar(tiemposUnidad)
print("Insert sort:",'\n')
mostrar(tiemposUnidad2)

# GRAFICA
#######Comparacion de tiempos reales######

fig2, ax2 = plt.subplots()
ax2.plot(tamanios, tiemposReal2, label='Insercion en tiempo real')
ax2.plot(tamanios, tiemposReal, label='Bubble en tiempo real')
ax2.set_xlabel('Tamaños de los arreglos')  # Add an x-label to the axes.
ax2.set_ylabel('Tiempo real')  # Add a y-label to the axes.
ax2.set_title("Comparacion de Bubble e Insert Sort en arreglos tipo " + elec)
ax2.legend()
ax2.grid()
fig2.savefig(elec + "_tiempo_real.png")

#######Comparacion en unidades de tiempo#####

fig, ax = plt.subplots()
ax.plot(tamanios, tiemposUnidad2, label='Insercion en unidades de tiempo')
ax.plot(tamanios, tiemposUnidad, label='Bubble en unidades de tiempo')
ax.set_xlabel('Tamaños de los arreglos')  
ax.set_ylabel('Tiempo en unidades')  # Add a y-label to the axes.
ax.set_title("Comparacion de Bubble e Insert Sort en arreglos tipo " + elec )
ax.legend()
ax.grid()
fig.savefig(elec + "_unidades_tiempo.png")


