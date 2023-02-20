import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 8888
BUFFER_SIZE = 1024

pong_bytes = "testUDP".encode()

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_socket.bind((HOST_IP, HOST_PORT))

print("UDP Server Up")

while (True):
	bytes_addr = udp_socket.recvfrom(BUFFER_SIZE)

	msg = bytes_addr[0]
	addr = bytes_addr[1]

	print("({}: {})".format(addr, msg))

	udp_socket.sendto(pong_bytes, addr)