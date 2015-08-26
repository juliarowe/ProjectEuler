#include <iostream>
using namespace std;

bool isFactor(long long int num, int x);
bool isPrime(int x);

int main(){

long long int thisNum = 600851475143;
int largestPfact = 0;

	for (long long int i = thisNum/2; i > 1; i = i-2)
	{
		if ((isFactor(thisNum, i)) && (isPrime(i))){
			largestPfact = i;
			break;
		}
	}
	
	cout << largestPfact << endl;

	return 0;
}

bool isFactor(long long int num, int x){
	if (num % x == 0) return true;
	else return false;
}

bool isPrime(int x){

	if (x < 2) return false;

	for (int i = 2; i < x/2; ++i)
	{
		if (isFactor(x, i)) return false;
	}

	return true;
}