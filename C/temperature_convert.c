#include <stdio.h>

int main() {
    float celsius, fahrenheit;

    // Solicita a entrada do usuário
    printf("Enter temperature in Celsius: ");
    scanf("%f", &celsius);

    // Converte para Fahrenheit usando a fórmula
    fahrenheit = (celsius * 9.0 / 5.0) + 32;

    // Exibe o resultado com duas casas decimais
    printf("%.2f°C is equal to %.2f°F\n", celsius, fahrenheit);

    return 0;
}
