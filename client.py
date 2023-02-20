import socket

msg_bytes = bytes(32)

server = ("127.0.0.1", 8888)
BUFFER_SIZE = 1024

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

client_socket.sendto(msg_bytes, server)

msg_server = client_socket.recvfrom(BUFFER_SIZE)

print("Server: {}".format(msg_server[0]))