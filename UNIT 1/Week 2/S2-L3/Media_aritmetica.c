#include <stdio.h>

int main() {
    float numero1, numero2;
    float media;
    
    //Chiede di inserire il primo numero
    printf("Inserisci il primo numero: ");
    scanf("%f", &numero1);
    
    //Chiede di inserire il secondo numero
    printf("Inserisci il secondo numero: ");
    scanf("%f", &numero2);
    
    //Calcola la media
    media = (numero1 + numero2) /2;
    
    //Mostra il risultato
    printf("La media dei due numeri è: %f\n", media);
    
    return 0;
}
