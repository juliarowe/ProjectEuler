#include <iostream>
using namespace std;

bool isPal(int num);
int DoingThings();

int main(){

	int answer = DoingThings();
	cout << answer << endl;
	
	
	return 0;
}

int DoingThings(){
	int biggestPal = 0;

	for (int i = 999; i >= 100 ; i--)
	{
		for (int j = 999; j >= 100 ; j--){
			if ((isPal(i*j)) && (i*j > biggestPal)){
			    biggestPal = i*j;
			}
		}
	}
	return biggestPal;
}

bool isPal(int num){

	int temp, firstDigit, revrs = 0;
	
	temp = num;
	
	while (temp > 0){
	    firstDigit = temp % 10;
	    temp = temp/10;
	    revrs = revrs*10 + firstDigit;
	}
	
	if (revrs == num) return true;
	else return false;

}