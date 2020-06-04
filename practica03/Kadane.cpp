#include <iostream>
#include <climits> 

using namespace std;

class VariableRetorno{
	public:
		int begin;
        int end;
        int sumaMaxima;	
};

VariableRetorno max_subarray_suma(int [],int );

int main() {
    int rutas,calles,valor;
    int maximo=0;
    cin >> rutas;
    int **M = new int* [rutas];
    int ArrCalles[rutas];
    int **ArrSumMaxIndices = new int*[rutas];

    //RESERVANDO MEMORIA PARA LA MATRIZ DE RESULTADOS
    for (int i = 0; i < rutas; i++)
    {
        ArrSumMaxIndices[i] = new int[3];
    }

    //LLENADO DE MATRIZ CON RUTAS Y CALLES
    for (int i = 0; i < rutas; i++){
        cin >> calles;
        ArrCalles[i]=calles;
        maximo= max(calles,maximo);
        M[i] = new int[calles];
        for(int j=0; j < calles-1;j++ ){
            cin>>valor;
            M[i][j]=valor;
        }
    }

    //MOSTRAR MATRIZ DE RUTAS Y CALLES
    cout << "Mostrar la matriz de RUTAS Y CALLES " << endl;
    for (int i = 0; i < rutas; i++) {
        for (int j = 0; j < maximo-1; j++)
            cout << M[i][j] << " ";
        cout << endl;
    }

   //HALLANDO LA SUMA MAX DE CADA RUTA Y LLENANDO RESULTADOS
   VariableRetorno result;
   for(int i=0;i<rutas;i++){
        result= max_subarray_suma(M[i],ArrCalles[i]);
        ArrSumMaxIndices[i][0]=result.begin;
        ArrSumMaxIndices[i][1]=result.end;
        ArrSumMaxIndices[i][2]=result.sumaMaxima;
   }

   //MOSTRAR MATRIZ CON RESULTADOS 
    cout << "Mostrar la matriz RESULTADO" << endl;
    for (int i = 0; i < rutas; i++) {
        for (int j = 0; j < 3; j++)
            cout << ArrSumMaxIndices[i][j] << " ";
        cout << endl;
    }

   //MOSTRANDO RESULTADOS
   for(int i=0;i< rutas;i++){
        if(ArrSumMaxIndices[i][2] <= 0){
            cout<<"La ruta "<<i+1<<" no tiene calles interesantes"<<endl;
        }
        else{
            cout<<"La mejor parte de la ruta "<<i+1<<" es entre las calles "<<ArrSumMaxIndices[i][0]<<" y "<<ArrSumMaxIndices[i][1]<<endl;
        }
   }

    delete [] M;
    delete [] ArrSumMaxIndices;

    return 0;
}

VariableRetorno max_subarray_suma(int arr[],int n){

	VariableRetorno variable;
	int sumamax=0;
    int suma=0;
	int e=0;
    int d=0;
    int x=0;
    for(int i=0;i<n;i++)
    {
  	    suma=suma+arr[i];						
	    if(suma<0){	
		    suma=0;
		    x=i+1;
		}
	    if(suma>sumamax){							
		    sumamax=suma;
		    e=x;
		    d=i;
		}
    }
    variable.begin=e+1;
    variable.end=d+2;
    variable.sumaMaxima=sumamax;
    return variable;
}
