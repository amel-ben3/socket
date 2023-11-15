import socket
import psycopg2
from psycopg2 import sql

# Paramètres de connexion à la base de données PostgreSQL
db_params = {
    'host': '127.0.0.1',
    'port': 5432,
    'user': 'postgres',
    'password': 'amel',
    'database': 'edi',
}

# Fonction pour récupérer une ligne de la table
def get_data_from_database():
    # Connexion à la base de données
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Exemple de requête pour récupérer une ligne de la table (remplacez avec votre propre requête)
    query = sql.SQL("SELECT * FROM \"Customer\" WHERE id=1")

    cursor.execute(query)

    # Récupérer la première ligne
    row = cursor.fetchone()

    # Fermer la connexion à la base de données
    cursor.close()
    connection.close()

    return row

# Fonction principale du serveur
def run_server():
    # Paramètres du serveur
    host = '127.0.0.1'
    port = 12345

    # Créer un socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Attendre au maximum 1 connexion en attente

    print(f"Le serveur écoute sur {host}:{port}...")

    while True:
        # Attendre une connexion
        client_socket, client_address = server_socket.accept()
        print(f"Connexion établie avec {client_address}")

        # Récupérer les données de la base de données
        data_from_database = get_data_from_database()

        # Envoyer les données au client
        client_socket.send(str(data_from_database).encode('utf-8'))

        # Fermer la connexion avec le client
        client_socket.close()

if __name__ == "__main__":
    run_server()
