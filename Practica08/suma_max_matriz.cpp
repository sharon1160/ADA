//Nombre : Sharon Chullunquía Rosas

#include <iostream>

using namespace std;

int sumAcum(int **A,int i,int j){
    if (i==0 && i==j){
        return A[i][j];
    }
    if (i==0 && j!=0){
        return(sumAcum(A,i,j-1)+A[i][j]);
    }
    if (i!=0 && j==0){
        return(sumAcum(A,i-1,j)+A[i][j]);
    }
    if (i!=0 && j !=0){
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
    if(fInf==0 && fInf==cInf){
        resultado = sumAcum(A,fSup,cSup);
        return resultado;
    }
    if (cInf == 0 && fInf != 0){
        resultado = sumAcum(A,fSup,cSup) - sumAcum(A,fInf-1,cSup);
        return resultado;
    }
    if (cInf != 0 && fInf ==0){
        resultado = sumAcum(A,fSup,cSup) - sumAcum(A,fSup,cInf-1);
        return resultado;
    }
    if (cInf != 0 & fInf != 0){
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

        for(int i = 0; i < n; i++){
            delete[] A[i]; 
        }
        delete[] A;
    }
    return 0;
}