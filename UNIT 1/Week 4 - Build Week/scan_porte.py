import socket
import re

def main():
    # Input dell'utente per l'indirizzo IP e il range di porte
    ip = input("Inserisci ip da scansire: ")
    port_range = input("Inserisci il range di porte (0-1024)")
    
    # Liste per porte chiuse e filtrate
    porte_chiuse = []
    porte_filtrate = []

    # Estrazione del range di porte
    low_port = (int(port_range.split('-')[0]))
    high_port = (int(port_range.split('-')[1]))
     
    # Scansione delle porte
    for port in range(low_port, high_port +1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

        s.settimeout(1)

        try:
            stato = s.connect_ex((ip, port))
            if stato == 0:
                try:
                    s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                    risposta = s.recv(1024).decode()
                    servizio = identifica_servizio(risposta)
                    print(f"Porta {port} aperta - servizio identificato: {servizio}")
                except Exception as e:
                    print(f"Porta {port} aperta - Impossibile identificare il servizio")
            else:
                if stato == 111:
                    porte_chiuse.append(port)
                else:
                    porte_filtrate.append(port)

        except Exception as e:
            print(f"Porta {port} - Errore: {e}")
        finally:
            s.close()
    
    # Richiesta per visualizzare le porte filtrate
    si_no = input("Vuoi la lista delle porte filtrate? S(Sì)/N(No): ")
    if(si_no.startswith("S")): print(f"Porte filtrate: {porte_filtrate}\n")
        
# Identificazione del servizio in base alla risposta del server
def identifica_servizio(risposta):
    if re.search(r'SSH', risposta, re.IGNORECASE):
        return "SSH"
    elif re.search(r'HTTP/1\.[01]', risposta):
        return "HTTP"
    elif re.search(r'SMTP', risposta, re.IGNORECASE):
        return "SMTP"
    elif re.search(r'FTP', risposta, re.IGNORECASE):
        return "FTP"
    elif re.search(r'IMAP', risposta, re.IGNORECASE):
        return "IMAP"
    elif re.search(r'POP3', risposta, re.IGNORECASE):
        return "POP3"
    elif re.search(r'Telnet', risposta, re.IGNORECASE):
        return "Telnet"
    elif re.search(r'DNS', risposta, re.IGNORECASE):
        return "DNS"
    else:
        return "Non riconosco il servizio"

if __name__ == "__main__":
    main()

Funzionamento del Codice
Input dell'utente: Richiede l'indirizzo IP e il range di porte da scansionare.
Scansione delle porte: Controlla ogni porta nel range specificato per vedere se è aperta, chiusa o filtrata.
Identificazione del servizio: Tenta di identificare il servizio in esecuzione sulla porta aperta basandosi sulla risposta ricevuta.
Output delle porte filtrate: Chiede all'utente se desidera visualizzare la lista delle porte filtrate e le stampa se richiesto.
