#include <iostream>
using namespace std;

int main(){
    double rad;
    double pi = 3.1415926535;
    string verse = "Im the king of NYC";
    cout << "What do you wan the radius to be? ";
    cin >> rad;
    double circumference = 2 * pi * rad;
    cout << "pi =" << endl;

    cout << pi << endl;
    cout << verse << endl;
    cout << "jk here's your answer for the circumference" << endl;
    cout << circumference << endl;
    cout << "btw circumference / perimeter of circle = 2pir or also 2 * pi * r" << endl;
    return 0;
}