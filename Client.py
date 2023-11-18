import socket

# Configuración del servidor
host = '0.0.0.0'  # Escucha en todas las interfaces disponibles
port = 12345       # Puerto de escucha

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al host y puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes (máximo 1 en espera)
server_socket.listen(1)

print(f"Esperando conexiones en {host}:{port}...")

# Aceptar la conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión aceptada desde {client_address}")

# Recibir datos y enviar una respuesta
data = client_socket.recv(1024)
print(f"Datos recibidos: {data.decode('utf-8')}")

response = "¡Conexión exitosa! Gracias por enviar datos."
client_socket.sendall(response.encode('utf-8'))

# Cerrar sockets
client_socket.close()
server_socket.close()
