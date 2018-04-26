
import socket
import time
#注意，udp接收端的地址为127.0.0.1时候不生效
address = ('127.0.0.1', 9876)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
	s.sendto(222)
	time.sleep(2)
	pass


s.close()
print("send udp")
