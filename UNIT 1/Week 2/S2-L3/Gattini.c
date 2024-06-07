#include <stdio.h>

void Gattino() {
    printf("     /\\_/\\\n");
    printf("    ( o.o )\n");
    printf("     > ^ <\n");
}

int main() {
    int scelta;
    float numero1, numero2, risultato;
   
    // Visualizza il menu
    printf("Scegli l'operazione da eseguire:\n");
    printf("1. Calcolare la media di due numeri\n");
    printf("2. Calcolare il prodotto di due numeri\n");
    printf("3. Mostrare un gattino\n");
    printf("Inserisci la tua scelta (1, 2 o 3): ");
    scanf("%d", &scelta);
   
    if (scelta == 1 || scelta == 2) {
        // Chiede di inserire i numeri
        printf("Inserisci il primo numero: ");
        scanf("%f", &numero1);
        printf("Inserisci il secondo numero: ");
        scanf("%f", &numero2);
    }
   
    // Esegue l'operazione scelta
    if (scelta == 1) {
        // Calcola la media
        risultato = (numero1 + numero2) / 2;
        printf("La media dei due numeri è: %f\n", risultato);
    } else if (scelta == 2) {
        // Calcola il prodotto
        risultato = numero1 * numero2;
        printf("Il prodotto dei due numeri inseriti è: %f\n", risultato);
    } else if (scelta == 3) {
        // Mostra il gattino
        Gattino();
    } else {
        printf("Scelta non valida. Riprova.\n");
    }

    return 0;
}
