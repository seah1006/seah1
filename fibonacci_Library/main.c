#include <stdio.h>
#include "fibonacci_Library.h"   

int main() {
    int n;

    printf("몇 번째 피보나치 수를 구할까요? : ");
    scanf("%d", &n);

    int result = fibonacci_iterative(n);   
    printf("%d번째 피보나치 수는 %d입니다.\n", n, result);

    return 0;
}
