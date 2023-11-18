import socket

# Configuración del cliente
host = 'IP_de_la_Raspberry_Pi'  # Reemplaza con la dirección IP de tu Raspberry Pi
port = 12345                      # Puerto de conexión

# Crear un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar datos al servidor
message = "Hola desde el cliente"
client_socket.sendto(message.encode('utf-8'), (host, port))

# Recibir la respuesta del servidor
data, server_address = client_socket.recvfrom(1024)
print(f"Respuesta del servidor ({server_address}): {data.decode('utf-8')}")

# Cerrar el socket del cliente
client_socket.close()
