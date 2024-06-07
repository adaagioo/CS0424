#include <stdio.h>

int main() {
    float numero1, numero2, prodotto;

    //Chiede all'utente di inserire il primo numero
    printf("Inserire il primo numero: ");
    scanf("%f", &numero1);

    //Chiede all'utente di inserire il secondo numero
    printf("Inserisci il secondo numero: ");
    scanf("%f", &numero2);

    //calcola il prodotto
    prodotto = numero1 * numero2;
    
    //Mostra il risultato del prodotto
    printf("Il prodotto dei due numeri inseriti è: %f\n", prodotto);
    
    return 0;
} 
