import socket
import time
# import base64

def startRelayServer():
	recvsock = socket.socket(sock.AF_INET, socket.SOCK_DGRAM)
	recvsock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST or socket.SO_REUSEADDR, 1)

	# Specify port, and ip address
	port = 3000
	host = 10.1.0.100

	try:
		recvsock.bind(("", int(port)))
	except Exception as e:
		print("Kill and restart this server and try again")
		print(e)
		return

	print("start to search on" + str(host))
	sendsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dstip = host
	sendsock.sendto(b"", ("127.0.0.1", port))
	while True:
		data, peer = recvsock.recvfrom(1024)
		if len(data) > 0 and port != peer[1]:
			port = peer[1]
			for i in range(3):
				sendsock.sendto(data, (dstip, peer[1]))
				print("sent to" + str(host) + "successfully")
				time.sleep(1)

if __name__ == "__main__":
	startRelayServer()
