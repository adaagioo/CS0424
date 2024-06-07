#include <stdio.h>

int main() {
    char scelta;
    char nome[25] = "Player";
    char risposta;
    int punteggio;

    // Presentazione del gioco
    printf("***************************************************************************\n");
    printf("            Benvenuti nel gioco più magico del mondo!\n         Giuro solennemente di non avere buone intenzioni!\n");
    printf("***************************************************************************\n");
        //Menù che ti chiede cosa vuoi fare
    do {
        printf("Scegli cosa vuoi fare:\n");
        printf("A) Iniziare una nuova partita\n");
        printf("B) Uscire dal gioco\n");
        printf("C) Magica sorpresa!\n");
        scanf(" %c", &scelta);  
        
        if (scelta != 'A' && scelta != 'a' && scelta != 'B' && scelta != 'b' && scelta != 'C' && scelta != 'c') {
            printf("Non capisco, sei un magonò!\n");
            continue;
        }
// se si sceglie la A allora iniziano le domande
        if (scelta == 'A' || scelta == 'a') {
            do {
                punteggio = 0;  //punto di reset di per partire sempre da 0
                printf("Prima di iniziare, qual è il tuo nome da mago o da strega?\n");//ti chiede di inserire un nome a cui ho dato una lunghezza massima 25 caratteri
                scanf("%s", nome);  
                printf("Dai %s, iniziamo!\n", nome);  

                printf("\nDomanda 1: Come si chiama il Preside di Hogwarts?\n");
                printf("A) Albus Silente\nB) Alberto Silente\nC) GianAlbus Silente\n");
                scanf(" %c", &risposta);  //registra la risposta data
                if (risposta == 'a' || risposta == 'A') { //Accetta sia risposta in minuscolo che in maiuscolo
                    printf("Esatto! Sei un mago!\n"); //Messaggio di risposta corretta
                    punteggio++; //Aumenta il punteggio
                } if (scelta != 'A' && scelta != 'a' && scelta != 'B' && scelta != 'b' && scelta != 'C' && scelta != 'c') {
                   printf("Non capisco, sei un magonò!\n");
                   continue;
                } else { //Altrimenti in caso di risposta sbagliata 
                    printf("Sbagliato, Babbano! Come fai a non conoscere il mago più potente del mondo magico A)Albus Silente\n");
                    
                }

                printf("\nDomanda 2: Chi è R.A.B?\n");
                printf("A) Regulos Arturo Black\nB) Regulus Arcturo Black\nC) Regulus Arcturus Black\n");
                scanf(" %c", &risposta);  
                if (risposta == 'c' || risposta =='C') {
                    printf("Esatto! Sei un mago!\n");
                    punteggio++;
                } if(scelta != 'A' && scelta != 'a' && scelta != 'B' && scelta != 'b' && scelta != 'C' && scelta != 'c') {
                   printf("Non capisco, sei un magonò!\n");
                   continue;
                }else {
                    printf("Sbagliato, Babbano! Come fai a non conoscere C) Regulus Arcturus Black\n");
                }

                printf("\nDomanda 3: Qual era il nome del villaggio dove risiedevano i Riddle?\n");
                printf("A) Little Hangleton\nB) Little Hollow\nC) Little Hallow\n");
                scanf(" %c", &risposta);  
                if (risposta == 'a' || risposta =='A') {
                    printf("Esatto! Sei un mago!\n");
                    punteggio++;
                } if(scelta != 'A' && scelta != 'a' && scelta != 'B' && scelta != 'b' && scelta != 'C' && scelta != 'c') {
                   printf("Non capisco, sei un magonò!\n");
                   continue;
                }else {
                    printf("Sbagliato, Babbano! L'antica famiglia Riddle che risiede a A) Little Hangleton\n");
                }

                printf("\nIl tuo punteggio parziale è: %d/3\n", punteggio);
                printf("\nVuoi giocare di nuovo? (s/n): ");
                scanf(" %c", &risposta);
            } while (risposta == 's' || risposta == 'S');

            printf("\nIl tuo punteggio finale è: %d/3\n", punteggio);
            printf("Fatto il Misfatto!\n");
        } else if (scelta == 'B' || scelta == 'b') {
            printf("Fatto il Misfatto!\n");
        } else if (scelta == 'C' || scelta == 'c') {
            printf("\nEcco la tua magica sorpresa:\n");
            printf("     /\\_/\\\n");
            printf("    ( o.o )\n");
            printf("     > ^ <\n");
            printf("  ___|___|____\n");
            printf(" /             \\\n");
            printf("|               |\n");
            printf(" \\_____________/\n");
        }

    } while (scelta != 'B' && scelta != 'b');

    return 0;
}
