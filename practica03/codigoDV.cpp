
int Seg_Max_DV(int arr[],int n){
	if(n==1){
		return arr[0];
	}
	int q=n/2;
	int izquierdaMax = Seg_Max_DV(arr,q);
	int derechaMax = Seg_Max_DV(arr+q,n-q);
	int suma_izquierda=INT_MIN;
	int suma_derecha=INT_MIN;
	int suma=0;
	for(int i= q;i<n;i++){
		suma += arr[i];
		suma_derecha=max(suma_derecha,suma);
	}
	suma=0;
	for(int i= (q-1);i>=0;i--){
		suma += arr[i];
		suma_izquierda=max(suma_izquierda,suma);
	}
	int ans = max(izquierdaMax,derechaMax);
	return max(ans,suma_izquierda + suma_derecha);
}
