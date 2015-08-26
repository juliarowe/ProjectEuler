#include <iostream>
using namespace std;

int addMultiples();
int main(){

	int sum = addMultiples();
	cout << "total: " << sum << endl;

	return 0;
}

int addMultiples()
{
	int sum = 0

	for (int n = 0; n< 1000; n++){
		if((n%3 == 0)||(n%5 ==0))){
			sum = sum + n;
		}
	}
	return sum;
}