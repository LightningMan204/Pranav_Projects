#include <iostream>
using namespace std;

int main(double pi, double rad){
    pi = 3.141592653;
    string verse = "Im the king of NYC";
    rad = 5.5;
    double circumference = 2 * pi * rad;
    cout << "pi =" << endl;

    cout << pi << endl;
    cout << verse << endl;
    cout << "jk here's your answer for the circumference" << endl;
    cout << circumference << endl;
    cout << "btw circumference / perimeter of circle = 2pir or also 2 * pi * r" << endl;
    return 0;
}