import socket
import struct
import time

# Configuración del cliente multicast
multicast_group = '224.1.1.1'
client_address = ('', 0)

# Crear un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configurar el socket para utilizar multicast
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                         struct.pack('4sL', socket.inet_aton(multicast_group), socket.INADDR_ANY))

# Vincular el socket al cliente y un puerto efímero
client_socket.bind(client_address)

# Establecer el tiempo de espera para la recepción de datos multicast
client_socket.settimeout(5)

# Enviar datos al grupo multicast
message = "Hola desde el cliente multicast"
client_socket.sendto(message.encode('utf-8'), (multicast_group, 12345))

try:
    while True:
        # Recibir la respuesta del servidor multicast
        data, address = client_socket.recvfrom(1024)
        print(f"Respuesta del servidor multicast ({address}): {data.decode('utf-8')}")

except socket.timeout:
    print("No se recibieron más mensajes multicast. Saliendo.")

finally:
    # Cerrar el socket del cliente
    client_socket.close()
