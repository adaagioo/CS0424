#include <stdio.h>   // Libreria per l'utilizzo degli standard I/O (Input/Output)
#include <stdlib.h>  // Libreria per le conversioni tra i tipi delle variabili e non solo
#include <string.h>  // Libreria per la manipolazione delle stringhe
#include <ctype.h>   // Libreria per la manipolazione dei caratteri


// Funzione contenente il menu
void printMenu() {
    printf("\n************************ Menu' ************************\n");
    printf("\n\t1. Programma che permette un segmentation fault\n");
    printf("\t2. Programma corretto\n");
    printf("\t3. Esci\n");
    printf("\n*******************************************************\n");
    printf("Scegli un numero: ");
}

// Funzione che gestisce il contrnuto di una stringa, richiede un puntatore come parametro
int Contenuto_stringa(const char *str){
    //per ogni carattere della stringa, verifica se ha all'interno caratteri diversi dai numeri
    //se sono tutti numeri, rilascia return 0 (classico true di python) se no, rilascia return 1
    for (int i = 0; str[i] != '\0'; i++){
        if (!isdigit(str[i])){
            return 0;
        }
    }
    return 1;
}

// Funzione Contenente il programma che permette il segmentation fault
void programmaSegmentationFault() {

    int vector[10], i, j, k;
    char Input_max[10];
    int swap_var;

    printf("Inserire 10 interi:\n");

    for (i = 0; i < 10; i++) {
        //inizia un loop infinito sul tipo di carattere che viene inserito nell'input utente iniziale
        int valid = 0;
        while (!valid){
            int c = i + 1;
            printf("[%d]:", c);
            scanf("%s",Input_max);
            //richiama la funzio e che ritorna true o false in base alla presenza di caratteri diversi dai numeri
            //se ritorna true, allora passa all'if successivo che controlla la massima lunghezza di un numero e genera
            //il segmantation fault se il n umero e' piu lungo di 10 miliardi, se non e' cosi lungo, allora inserisce 
            //all'interno del vettore 'vector' i valori iniziali presi da input sotto forma di numeri perche inizialmente 
            //vengono scritti come strighe 
            if (Contenuto_stringa(Input_max)){

                if (strlen(Input_max) > 10){
			        vector[1000000] = 0;
		        } else {
                    //questa parte serve per far funzionare correttamente la 'stampa' (output su termiale) dei numeri scelti
                    //che avverra' in seguito
                    vector[i] = atoi(Input_max);
                }
            //se invece ritorna false, allora avvisa di inserire solo numeri fino a quando non verrano appunto inseriti
            } else {
                printf("riprova. accetta solo numeri interi\n");
            }
        }
    }

    printf("Il vettore inserito e':\n");
    for (i = 0; i < 10; i++) {
        int t = i + 1;
        printf("[%d]: %llu\n", t, vector[i]);
    }


    for (j = 0; j < 10 - 1; j++) {
        for (k = 0; k < 10 - j - 1; k++) {
            if (vector[k] > vector[k + 1]) {
                swap_var = vector[k];
                vector[k] = vector[k + 1];
                vector[k + 1] = swap_var;
            }
        }
    }

    printf("I primi 10 numeri ordinati sono:\n");
    for (j = 0; j < 10; j++) {
        int g = j + 1;
        printf("[%d]: %llu\n", g, vector[j]);
    }

}

//Funzione che contiene il codice corretto
void programmaCorretto() {
    //utilizzo di variabili che possono contenere + bit del solito per prevenire il segmentation fault
    unsigned long long int vector[10];
    int i, j, k;
    unsigned long long int swap_var;

    printf("Inserire 10 interi:\n");

    for (i = 0; i < 10; i++) {
        int c = i + 1;
        printf("[%d]:", c);

        unsigned long long int MAX = 1844674407370955161;

        //Impedisce di usare numeri piu' lunghi della stessa lunghezza massima dell'unsigned long long int
        while(scanf("%llu", &vector[i]) != 1 || vector[i] > MAX){
            printf("Riprova, accetta solo numeri interi validi e non superiori a %llu\n", MAX);
            int ch;
            // pulisce il buffer dell'input
            while ((ch = getchar()) != '\n' && ch != EOF);
            printf("[%d]: ", c);
        }
    }

    printf("Il vettore inserito e':\n");
    for (i = 0; i < 10; i++) {
        int t = i + 1;
        printf("[%d]: %llu\n", t, vector[i]);
    }


    for (j = 0; j < 10 - 1; j++) {
        for (k = 0; k < 10 - j - 1; k++) {
            if (vector[k] > vector[k + 1]) {
                swap_var = vector[k];
                vector[k] = vector[k + 1];
                vector[k + 1] = swap_var;
            }
        }
    }

    printf("I primi 10 numeri ordinati sono:\n");
    for (j = 0; j < 10; j++) {
        int g = j + 1;
        printf("[%d]: %llu\n", g, vector[j]);
    }
}

// Funzione main finale contenente tutte le funzioni precedenti
int main() {
    int scelta;
    int risultato;

    // Loop do-while per fa funzionare il programma all'infinito, con la possibilita' dell'uscita manuale
    do {
        printMenu();
        risultato = scanf("%d", &scelta);

        while (getchar() != '\n'); //pulisce l'input

        if (risultato != 1) {
            printf("Accetta solo numeri, riprova\n");
            continue;
        }

        switch (scelta) {
            case 1:
                programmaSegmentationFault();
                break;
            case 2:
                programmaCorretto();
                break;
            case 3:
                printf("Uscita dal programma.\n");
                break;
            default:
                printf("\nAccetta solo numeri compresi tra 0 e 3, naturali. Riprova.\n");
                break;
        }
    } while (scelta != 3 );

    return 0;
}
