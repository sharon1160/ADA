//Nombre : Sharon Chullunquía Rosas

#include <iostream>

using namespace std;

int sumAcum(int **A,int i,int j){
    //Caso base
    if (i==0 && i==j){
        return A[i][j];
    }
    //Primer caso
    if (i==0 && j!=0){
        return(sumAcum(A,i,j-1)+A[i][j]);
    }
    //Segundo caso
    if (i!=0 && j==0){
        return(sumAcum(A,i-1,j)+A[i][j]);
    }
    //Tercer caso
    if (i!=0 && j !=0){
        //A[i,j] = sumatoria de los elementos hasta el indice i,j
        //        = Orig[i,j] + A[i,j-1] + A[i-1,j] - A[i-1,j-1]
        return (A[i][j] + sumAcum(A,i,j-1)+ sumAcum(A,i-1,j)-sumAcum(A,i-1,j-1));
    }
}

/*

Donde : 

fInf : fila inferior
cInf : columna inferior
fSup : fila superior
cSup : columna superior

*/

int sumaMatriz(int **A,int fInf,int cInf,int fSup ,int  cSup){
    int resultado;
    //Primer caso
    if(fInf==0 && fInf==cInf){
        resultado = sumAcum(A,fSup,cSup);
        return resultado;
    }
    //Segundo Caso
    if (cInf == 0 && fInf != 0){
        resultado = sumAcum(A,fSup,cSup) - sumAcum(A,fInf-1,cSup);
        return resultado;
    }
    //Tercer Caso
    if (cInf != 0 && fInf ==0){
        resultado = sumAcum(A,fSup,cSup) - sumAcum(A,fSup,cInf-1);
        return resultado;
    }
    //Cuarto Caso
    if (cInf != 0 & fInf != 0){
        //resultado = z - p - q + r
        resultado = sumAcum(A,fSup,cSup) - sumAcum(A,fInf-1,cSup) - sumAcum(A,fSup,cInf-1) + sumAcum(A,fInf-1,cInf-1);
        return resultado;
    }
}

int suma_maxima(int **A,int n){
    int resultado;
    int sumMax = 0;
    for(int fInf = 0; fInf < n; fInf++){
        for(int cInf = 0; cInf < n; cInf++){
            for(int fSup = fInf; fSup < n; fSup++){
                for(int cSup = cInf; cSup < n; cSup++){
                    resultado = sumaMatriz(A, fInf, cInf, fSup, cSup);
                    if( sumMax < resultado)
                       sumMax = resultado;
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
                if(A[i][j] >= 1000){
                    flag = false;
                    break;
                }
            }
            if(flag == false)
                break;
        }

        if(flag == true){
            int resultado;
            resultado = suma_maxima(A,n);
            cout<<resultado<<endl;
        }
        else{
            cout<<"Valores fuera del rango establecido 0<=|n|<1000"<<endl;
        }

        for(int i = 0; i < n; i++){
            delete[] A[i]; 
        }
        delete[] A;
    }
    return 0;
}

/*
Para compilar :

g++ suma_max_matriz.cpp -o suma_max_matriz.out
./suma_max_matriz.out < prueba.txt > resultado.txt
*/