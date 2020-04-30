//BUBBLE SORT

#include <bits/stdc++.h> 
using namespace std; 

void swap(int *xp, int *yp) 
{ 
	int temp = *xp; 
	*xp = *yp; 
	*yp = temp; 
} 

// A function to implement bubble sort 
void bubbleSort(int arr[], int n) 
{ 
    int asig=0;//# de asignaciones
    int compa=0;//# de comparaciones
    int objeto=0;//# de creaciones de objetos
    int memoria=0;//# de veces que separa memoria para un arreglo o lista de tamanho 'n' 

	int i, j; 
  objeto+=2;//por la creacion de los enteros i y j
  asig++;//por el valor cero que toma i en el for
	for (i = 0; i < n-1; i++,asig++){//el asig++ por el i++	 
         // Last i elements are already in place
        compa++;//comparacion del for
        asig++;//por el valor cero que toma j en el for
        for (j = 0; j < n-i-1; j++,asig++){//el asig++ por el i++
            compa+=2;//comparacion del for y del if
            if (arr[j] > arr[j+1]) 
                swap(&arr[j], &arr[j+1]);
                asig+=3;//las asignaciones que hay dentro del swap
                objeto++;//la creacion de un entero dentro del swap
        }
        compa++;//la ultima comparacion que no cumple la condicion del for
    }
    compa++;//la ultima comparacion que no cumple la condicion del for

    asig=asig*8;
    compa=compa*2;
    objeto=objeto*200;
    //memoria=memoria*50 + n* 10

    cout<<"Numero de asignaciones: "<<asig<<endl;
    cout<<"Numero de comparaciones: "<<compa<<endl;
    cout<<"Numero de creaciones de objeto: "<<objeto<<endl;
    cout<<"Numero de asignaciones de memoria: "<<memoria<<endl;
} 

/* Function to print an array */
void printArray(int arr[], int size) 
{ 
	int i; 
	for (i = 0; i < size; i++) 
		cout << arr[i] << " "; 
	cout << endl; 
} 

// Driver code 
int main() 
{ 
	int arr[] = {64, 34, 25, 12, 22, 11, 90}; 
	int n = sizeof(arr)/sizeof(arr[0]); 
	bubbleSort(arr, n); 
	cout<<"Sorted array: \n"; 
	printArray(arr, n); 
	return 0; 
} 

//Fuente:geeksforgeeks 
