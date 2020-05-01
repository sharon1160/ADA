//INSERT SORT

#include <bits/stdc++.h> 
using namespace std; 

/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n) 
{   
	int asig=0;//# de asignaciones
	int compa=0;//# de comparaciones
	int objeto=0;//# de creaciones de objeto
	int memoria=0;//# de veces que separa memoria para un arreglo o lista de tamanho 'n'

	int i, key, j;
	objeto+=3;//la creacion de tres objetos i,j y key
	asig++;//por la asignacion de i=1 en el for
	for (i = 1; i < n; i++,asig++) //el asig++ por el i++
	{ 
        	compa++;//por la comparacion del for
		key = arr[i]; 
		j = i - 1;
		asig+=2; //por las asignaciones de key y j
		
		/* Move elements of arr[0..i-1], that are 
		greater than key, to one position ahead 
		of their current position */
		while (j >= 0 && arr[j] > key) 
		{ 
			compa+=2;//las dos comparaciones que estan dentro del while
			arr[j + 1] = arr[j]; 
			j = j - 1; 
			asig+=2;//por las dos asignaciones anteriores
		}
		compa+=2;// por las ultimas dos comparaciones que no cumpliran con la condicion del while
		arr[j + 1] = key;
		asig++; //por la anterior asignacion
	} 
	compa++;// por la ultima comparacion que no cumplira con la condicion del for 

	asig=asig*8;
	compa=compa*2;
	objeto=objeto*200;
	//memoria=memoria*50 + n* 10

	cout<<"Numero de asignaciones: "<<asig<<endl;
	cout<<"Numero de comparaciones: "<<compa<<endl;
	cout<<"Numero de creaciones de objeto: "<<objeto<<endl;
	cout<<"Numero de asignaciones de memoria: "<<memoria<<endl;
} 

// A utility function to print an array of size n 
void printArray(int arr[], int n) 
{ 
	int i; 
	for (i = 0; i < n; i++) 
		cout << arr[i] << " "; 
	cout << endl; 
} 

/* Driver code */
int main() 
{ 
	int arr[] = { 12, 11, 13, 5, 6 }; 
	int n = sizeof(arr) / sizeof(arr[0]); 

	insertionSort(arr, n); 
	printArray(arr, n); 

	return 0; 
} 

//Fuente:geeksforgeeks
