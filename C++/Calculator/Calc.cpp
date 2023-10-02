#include<iostream>
#include<stdio.h>

using namespace std;
int main() {
    char oper;
    double num1,num2;

    cout << "Enter Two Numbers: ";
    cin >> num1 >> num2;

    cout << "Enter The Operator ( +, -, *, / ) : ";
    cin >> oper;

    switch (oper){

        case '+':
            cout << num1 << " + " << num2 << " = " << (num1 + num2);
            break;

        case '-':
            cout << num1 << " - " << num2 << " = " << (num1 - num2);
            break;

        case '*':
            cout << num1 << " * " << num2 << " = " << (num1 * num2);
            break;

        case '/':
            if (num2 != 0.0)
                cout << num1 << " / " << num2 << " = " << (num1 / num2);
            else
                cout << "Cannot divide by zero idiot, didn't you learn that in 2nd grade?";
            break;
        
        default:
            cout << oper << "Invalid option";
            break;

    }


    return 1;
}