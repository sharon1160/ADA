\\Nombre : Sharon Chullunquía Rosas

#include <iostream>
#include <bits/stdc++.h> 

using namespace std;

int partition(int arr[], int low, int high) 
{ 
    int pi = arr[high];
    int i = low; 
    for (int j = low; j <= high - 1; j++) { 
        if (arr[j] <= pi){ 
            swap(arr[i], arr[j]); 
            i++; 
        } 
    } 
    swap(arr[i], arr[high]); 
    return i; 
} 

int small_element(int arr[], int low, int high, int k) { 

    if (k > 0 && k <= high - low + 1) { 
        int pos = partition(arr, low, high); 

        if (pos - low == k - 1) 
            return arr[pos]; 
        if (pos - low > k - 1)  
            return small_element(arr, low, pos - 1, k); 
            
        return small_element(arr, pos + 1,high, k - pos + low - 1); 
    } 
    return INT_MAX; 
} 
  
int main(){
    int n,medio;
    cin>>n;
    int A[n];
    do{
        for(int i=0;i<n;i++){
               cin>>A[i];
        }
        medio=((n-1)/2)+1;
        cout<<small_element(A,0,n-1,medio)<<endl;
    }while(cin>>n);
    return 0;
}
