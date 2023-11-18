import socket

# Configuración del cliente
host = 'IP_de_la_Raspberry_Pi'  # Reemplaza con la dirección IP de tu Raspberry Pi
port = 12345                      # Puerto de conexión

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((host, port))
print(f"Conectado a {host}:{port}")

# Enviar datos al servidor
message = "Hola desde el cliente"
client_socket.sendall(message.encode('utf-8'))

# Recibir la respuesta del servidor
data = client_socket.recv(1024)
print(f"Respuesta del servidor: {data.decode('utf-8')}")

# Cerrar el socket del cliente
client_socket.close()
