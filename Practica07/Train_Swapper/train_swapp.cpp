//Nombre : Sharon Chullunquía Rosas

#include <iostream>
#include <vector>

using namespace std;

void quickSort(vector<int>& arr,int low,int high);

int nSwaps;

int main(int argc, char const *argv[])
{
    vector<int> arr;
    int cant_trenes;
    int cant_vagones;
    int vagon;
    while(cin>>cant_trenes){
        for(int i = 0; i < cant_trenes; i++){
            nSwaps =0;
            arr.clear();
            cin >> cant_vagones;
            for(auto j = 0; j < cant_vagones; j++){
                cin>>vagon;
                arr.push_back(vagon);
            }
            quickSort(arr,0,arr.size()-1);
            cout << "La mejor cantidad de swaps de trenes es "<< nSwaps << " swaps" << endl;
        }
    }
}

void swap(int* a, int* b)  
{  
    int t = *a;  
    *a = *b;  
    *b = t; 
}  
  
int partition (vector<int>& arr, int low, int high)  
{  
    int pivot = arr[high];
    int i =low-1;
  
    for (int j = low; j <= high - 1; j++)  
    {  
        if (arr[j] < pivot )  
        {  
            i++;
            swap(&arr[i], &arr[j]);
            if(i!=j)
              nSwaps++;   
        }  
    }  
    swap(&arr[i + 1], &arr[high]);
    if(i+1!=high)
        nSwaps++;
    return (i + 1);  
}  
  
void quickSort(vector<int>& arr, int low, int high)  
{  
    if (low < high)  
    {  
        int pi = partition(arr, low, high);  
        quickSort(arr, low, pi - 1);  
        quickSort(arr, pi + 1, high);  
    }  
}

/*
EJEMPLO DE ENTRADA

3
3
1 3 2
4
4 3 2 1
2
2 1

PARA COMPILAR

g++ train_swapper.cpp -o train_swapper.out
./train_swapper.out < test.txt > resultado.txt

*/
