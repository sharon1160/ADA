//Nombre : Sharon Chullunquía Rosas

//Codigo hecho con programación dinamica

#include <iostream>
#include <cmath>

using namespace std;

/*

Donde : 

fInf : fila inferior
cInf : columna inferior
fSup : fila superior
cSup : columna superior

*/

int suma_maxima(int **A,int n){
    int Subsuma_resultado;
    int sumMax = -999*pow(n,2); //el valor mas pequenio que puede tomar
    for(int fInf = 0; fInf < n; fInf++){
        for(int cInf = 0; cInf < n; cInf++){
            for(int fSup = fInf; fSup < n; fSup++){
                for(int cSup = cInf; cSup < n; cSup++){
                    Subsuma_resultado = A[fSup][cSup];// O(1)
                    if(fInf > 0)
                        Subsuma_resultado -= A[fInf-1][cSup];
                    if(cInf > 0)
                        Subsuma_resultado -= A[fSup][cInf-1];
                    if(fInf > 0 && cInf > 0)
                        Subsuma_resultado += A[fInf-1][cInf-1];
                    sumMax = max(sumMax, Subsuma_resultado);
                }
            }
        }
    }
    return sumMax;
}


int main (){
    int n;
    bool flag = true;
    cin>>n;
    if (0<n && n<128){

        int **A = new int* [n];
        for (int i = 0; i < n; i++){
            A[i] = new int[n];
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cin>>A[i][j];
                //Los valores dentro de la matriz están entre 0<=|n|<1000
                if(A[i][j] >= 1000 || A[i][j] <= -1000){
                    flag = false;
                    break;
                }
            }
            if(flag == false)
                break;
        }

        if(flag == true){
            int resultado;
            //Hallando matriz de suma acumulativa  sobre la matriz original
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (i > 0) 
                        A[i][j] += A[i - 1][j];
                    if (j > 0) 
                        A[i][j] += A[i][j - 1];
                    if (i > 0 && j > 0)
                        A[i][j] -= A[i - 1][j - 1];
                }
            }
            resultado = suma_maxima(A,n);
            cout<<resultado<<endl;
        }
        else
            cout<<"Valores fuera del rango establecido 0<=|n|<1000"<<endl;

        for(int i = 0; i < n; i++){
            delete[] A[i]; 
        }
        delete[] A;
    }
    return 0;
}

/*
Para compilar :

g++ suma_max_matriz_pd.cpp -o suma_max_matriz_pd.out
./suma_max_matriz_pd.out < prueba1.txt > resultado1.txt
*/