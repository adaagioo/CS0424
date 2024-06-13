import math
 
# Funzione che calcola il perimetro del quadrato dato il lato
def perimetro_quadrato(lato):
    return lato * 4
  
# Funzione per la circonferenza dato il raggio
def perimetro_cerchio(raggio):
    return 2 * math.pi * raggio
  
# Funzione per il perimetro del rettangolo dato base e altezza
def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)
  
# Funzione per richiedere e verificare che l'input sia valido
def richiedi_float(messaggio):
    while True:
        try: #richiede l'input e lo converte in float
            valore = float(input(messaggio))
            if valore < 0:
                raise ValueError("Il valore deve essere un numero positivo.")
            return valore
        except ValueError as e:
            #Gestisce gli errori di input e richiede nuovamente l'input.
            print(f"Errore di input: {e}. Riprova.")
          
# Funzione principale che gestisce il menù
def main():
    while True:
        # Mostra il menù
        print("Scegli una figura geometrica per calcolare il perimetro:")
        print("1. Quadrato")
        print("2. Cerchio")
        print("3. Rettangolo")
        print("4. Gattino matematico")
        print("5. Esci")
# Richiede la scelta dell'utente
        scelta = input("Inserisci il numero della tua scelta: ")
      
# Gestisce le varie scelte date in input dall'utente
        if scelta == '1':
            lato = richiedi_float("Inserisci la lunghezza del lato del quadrato: ")
            print(f"Il perimetro del quadrato è: {perimetro_quadrato(lato)}")
        elif scelta == '2':
            raggio = richiedi_float("Inserisci il raggio del cerchio: ")
            print(f"La circonferenza del cerchio è: {perimetro_cerchio(raggio)}")
        elif scelta == '3':
            base = richiedi_float("Inserisci la lunghezza della base del rettangolo: ")
            altezza = richiedi_float("Inserisci l'altezza del rettangolo: ")
            print(f"Il perimetro del rettangolo è: {perimetro_rettangolo(base, altezza)}")
        elif scelta == '4':
            print("Ecco un gattino matematico!")
            print("""
              /\\_/\\  
             ( o.o ) 
              > ^ <
            /---------\\
            | 2 + 2 = 4 |
            \\---------/
            """)
        elif scelta == '5':
            print("What's the offial animal of Pi day? The Py-thon! Ciao!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
