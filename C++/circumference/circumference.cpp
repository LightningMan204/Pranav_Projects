#include <iostream>
using namespace std;

void area(){
    string yn;
    cout << "Do you want to calculate the area of the circle? y or n\n";
    cin >> yn;
    switch(yn){
        case "y":
       
    }
}






int main(){
    double rad;
    double pi = 3.141592653589793;
    string verse = "Im the king of NYC";
    cout << "What do you want the radius of the circle to be? ";
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
