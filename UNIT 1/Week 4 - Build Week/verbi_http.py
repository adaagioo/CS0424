import requests


def main():
    # Input dell'utente per l'host e la porta
    host = input("Inserisci url dell'host: ")
    porta = input("Inserisci porta: ")
    
    # Costruzione dell'URL in base alla porta
    if porta == "80":
        url = f"http://{host}:{porta}"
    elif porta == "443":
        url = f"https://{host}:{porta}"
    else:
        print("Controlla la porta inserita!")
        return

    # Stampa dell'URL verificato
    print(f"Verifico: {url}")

    try:
        # Invio della richiesta HTTP OPTIONS
        risposta = requests.options(url)
        # Controllo del codice di stato della risposta
        if risposta.status_code == 200:
             # Controllo se l'intestazione 'Allow' è presente nella risposta
            if 'Allow' in risposta.headers:
                metodi = risposta.headers['Allow']
                print(f"Ecco i metodi abilitati: {metodi}")
            else:
                print("Allow non è presente nella risposta\n")
        else:
            print(f"Codice di stato: {risposta.status_code}")
    except requests.RequestException as e:
         # Gestione delle eccezioni per errori nella richiesta
        print(f"Errore nella richiesta: {e}")



if __name__ == "__main__":
    main()

