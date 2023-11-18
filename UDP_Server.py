import socket

# Configuración del servidor
host = '0.0.0.0'  # Escucha en todas las interfaces disponibles
port = 12345       # Puerto de escucha

# Crear un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular el socket al host y puerto
server_socket.bind((host, port))

print(f"Esperando datagramas en {host}:{port}...")

while True:
    # Recibir datos y la dirección del cliente
    data, client_address = server_socket.recvfrom(1024)
    print(f"Datos recibidos de {client_address}: {data.decode('utf-8')}")

    # Enviar una respuesta al cliente
    response = "¡Datagrama recibido con éxito!"
    server_socket.sendto(response.encode('utf-8'), client_address)
