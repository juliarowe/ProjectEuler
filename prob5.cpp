#include <iostream>
using namespace std;

bool isFactor(int num, int x);
bool isPrime(int x);
int findNum();

int main(){

	cout << findNum() << endl;
	return 0;
}


bool isFactor(int num, int x){
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

int findNum(){

	vector<int> primeLT20;

	for (int i = 1; i <= 20; ++i){
		if isPrime(i){
			primeLT20.push_back(i);
		}
	}

	vector<int> temp = PrimesLT20
	bool found = false
	bool factors = true
	int x= 2520

	while (!found){
		while (((temp.size) > 0) && (factors)){
			if ((x % temp.pop()) == 0) factors = true;
			else factors = false
		}
		if (factors) found = true;
		else x = x+1;
	}

	return x;
}