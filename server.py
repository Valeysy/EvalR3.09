"https://github.com/Valeysy/EvalR3.09"


import socket
import threading

class GestionServeur:
    
    def __init__(self, hote, port, max_clients, ui):
        self.hote = hote
        self.port = port
        self.max_clients = max_clients
        self.ui = ui
        self.socket_serveur = None
        self.en_marche = False
        self.threads_clients = []
        self.connexions_clients = []

    def demarrer(self):
        self.socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_serveur.bind((self.hote, self.port))
        self.socket_serveur.listen(self.max_clients)
        self.en_marche = True
        self.ui.afficher_message(f"Serveur démarré sur {self.hote}:{self.port}")
        threading.Thread(target=self.accepter_clients, daemon=True).start()

    def accepter_clients(self):
        while self.en_marche:
            client_socket, adresse_client = self.socket_serveur.accept()
            self.ui.afficher_message(f"Client connecté : {adresse_client}")
            thread_client = threading.Thread(target=self.gerer_client, args=(client_socket, adresse_client))
            thread_client.start()
            self.threads_clients.append(thread_client)
            self.connexions_clients.append(client_socket)

    def gerer_client(self, client_socket, adresse_client):
        try:
            while self.en_marche:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                if message == "deco-server":
                    break
                self.ui.afficher_message(f"{adresse_client} : {message}")
        except Exception as e:
            self.ui.afficher_message(f"Erreur avec le client {adresse_client} : {e}")
        finally:
            client_socket.close()
            self.ui.afficher_message(f"Client déconnecté : {adresse_client}")
            if client_socket in self.connexions_clients:
                self.connexions_clients.remove(client_socket)

    def arreter(self):
        self.en_marche = False
        if self.socket_serveur:
            self.socket_serveur.close()
        for client_socket in self.connexions_clients:
            client_socket.close()
        for thread in self.threads_clients:
            thread.join()
        self.ui.afficher_message("Le serveur est arrêté.")
