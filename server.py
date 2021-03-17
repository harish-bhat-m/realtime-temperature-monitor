import os
import sys
#import thread
import threading
import socket


class TempServer(object):
	""" Temperature Server which initialises the host name/ip and port.
		and binds the server.
		Returns the socket object
	"""
	def __init__(self, host, port):
		"""Constructor
		"""
		self.host = host
		self.port = port
				
	def server_bind(self,l=5):
		""" Initializes the socket and binds the host and port and returns
			the socket object
		"""
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.bind((self.host, self.port))
			self.sock.listen(l)
			return self.sock
		except Exception as err:
			print(err)
			sys.exit(0)
			
		
class TempMonitor(threading.Thread):
	""" Implementation of Threading to sever multiple clients
	"""
	def __init__(self,conn, addr):
		"""Initialization
		"""
		threading.Thread.__init__(self)
		self.connection = conn
		self.addrress = addr
				
	def run(self):
		""" Display the data for each city
		"""
		while True:
			try:
				data = self.connection.recv(1024)
				if not data:
					break
				else:
					print(data.decode())
			except socket.error as sock_error:
				break
		return 0

		
def main(host, port):
	""" Main Programm which will initiate the thread for each connection
	"""
	print ("Server Started")
	server = TempServer(host,port)
	sock = server.server_bind(l=10)
	while True:
		try:
			conn,addr = sock.accept()
			t=TempMonitor(conn,addr)
			t.start()
		except KeyboardInterrupt as err_msg:
			print ("Server is going down")
			conn.close()
			sock.close()
			sys.exit(0)
	


if __name__ == "__main__":
	host = "127.0.0.1"
	port = 53000
	main(host,port)
