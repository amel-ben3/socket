import socket

def run_client():
    # Paramètres du serveur
    host = '127.0.0.1'
    port = 12345

    # Créer un socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Se connecter au serveur
        client_socket.connect((host, port))
        print(f"Connecté au serveur sur {host}:{port}")

        # Recevoir les données du serveur
        data = client_socket.recv(1024)
        print(f"Données reçues du serveur : {data.decode('utf-8')}")

    finally:
        # Fermer la connexion avec le serveur
        client_socket.close()

if __name__ == "__main__":
    run_client()
