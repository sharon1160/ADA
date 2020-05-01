//GENERADOR

/*
1] Crear un generador de arreglos
10 / 1mil / 100 mil / 1 millón*/

#include <iostream>

using namespace std;
 
int main ()
{
    int array[1000000];
    int cant;
    cout<<"Ingrese la cantidad de numeros del arreglo a generar:"<<endl;
    cin>>cant;
    //Llenando el array con numeros aleatorios y mostrando el array generado
    int numero;
    cout<<"El array generado es:"<<endl ;
    for(int i=0 ;i<cant;i++)
    {
        numero= rand()% 101;//numeros aleatorios del 1 al 100
        array[i]=numero;
        cout <<array[i]<<" ";
    }
    cout<<endl;
    return 0;
}
