import socket

def demarrer_client(hote, port=4200):
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hote, port))
    print("Connecté au serveur.")
    while True:
        message = input("Client : ")
        if message.lower() == "quit":
            break
        client_socket.send(message.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    demarrer_client('localhost')
