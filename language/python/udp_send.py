
import socket
import time

address = ('127.0.0.0', 9876)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
	s.sendto(222)
	time.sleep(2)
	pass


s.close()
print("send udp")
