#include <iostream>
#include <math.h>
using namespace std;
int main(){
    double num;
    double power;
    cout << "Hello\n";
    cout << "What do you want the number to be? \n";
    cin >> num;
    cout << "What power do you want to be given? \n";
    cin >> power;
    cout << num << " To the " << power << " = " << pow(num, power);
    return 0;
}