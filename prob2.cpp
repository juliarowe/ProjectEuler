#include <iostream>
using namespace std;

int nthFibonacci(int n);
bool isEven(int n);
int sumEvenFib();

int main(){

	int sum = sumEvenFib();
	cout << sum << endl;
	return 0;
}

int nthFibonacci(int n){

	if (n == 1) return 1;
	if (n == 2) return 2;

	return nthFibonacci(n-1) + nthFibonacci(n-2);


}

bool isEven(int n){

	if(n%2 == 0) return true;
	else return false;

}

int sumEvenFib(){

	int sum = 0;

	for (int n = 1; nthFibonacci(n) < 4000000; n++){
		if (isEven(nthFibonacci(n))){
		    sum += nthFibonacci(n);
		}
	}
	
	return sum;
}