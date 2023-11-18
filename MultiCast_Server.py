import socket
import struct

# Configuración del servidor multicast
multicast_group = '224.1.1.1'
server_address = ('', 12345)

# Crear un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configurar el socket para utilizar multicast
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                         struct.pack('4sL', socket.inet_aton(multicast_group), socket.INADDR_ANY))

# Vincular el socket al host y puerto
server_socket.bind(server_address)

print(f"Esperando mensajes multicast en {multicast_group}:{server_address[1]}...")

while True:
    # Recibir datos
    data, address = server_socket.recvfrom(1024)
    print(f"Datos recibidos de {address}: {data.decode('utf-8')}")
