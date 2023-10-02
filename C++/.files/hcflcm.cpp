#include <iostream>

// Function to calculate GCD (HCF) of two numbers
int calculateGCD(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to calculate LCM of two numbers
int calculateLCM(int a, int b) {
    return (a * b) / calculateGCD(a, b);
}

int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    int numbers[n];
    for (int i = 0; i < n; ++i) {
        std::cout << "Enter number " << i + 1 << ": ";
        std::cin >> numbers[i];
    }

    int hcf = numbers[0];
    int lcm = numbers[0];

    for (int i = 1; i < n; ++i) {
        hcf = calculateGCD(hcf, numbers[i]);
        lcm = calculateLCM(lcm, numbers[i]);
    }

    std::cout << "HCF (GCD) of the numbers: " << hcf << std::endl;
    std::cout << "LCM of the numbers: " << lcm << std::endl;

    return 0;
}
