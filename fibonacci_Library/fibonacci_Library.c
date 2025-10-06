#include "fibonacci_Library.h"


int fibonacci_iterative(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, result;
    for (int i = 2; i <= n; i++) {
        result = a + b;
        a = b;
        b = result;
    }
    return b;
}

