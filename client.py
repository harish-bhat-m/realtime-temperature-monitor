import os
import sys
import random
import socket
import time

class Climate(object):
	""" Main class for Climate. 
		Temperature Generation
	"""
	def __init__(self):
		self.city = ""
		self.temp = ""

	def get_city(self):
		""" Get the city name
		"""
		try:
			self.city = str(input("Enter the city name:"))
		except Exception as error_msg:
			print ("Error in input")
			sys.exit(0)

	def take_temperature(self):
		""" Generates the temperature and bidns the cit name to it.
		"""
		try:
			self.temp = str(round(random.uniform(0,40),2))
			temp_str = "{0}\t{1}".format(self.city,self.temp)
			print(temp_str)
			return temp_str.encode()
			
		except Exception as err_msg:
			print ("Error in generating the temperature")
			sys.exit(0)

class Client(object):
	""" Implementation of client socket
	"""

	def __init__(self,host, port):
		self.host = host
		self.port = port

	def connect_server(self):
		""" Connects the client with server
		"""
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((self.host,self.port))
			return sock
		except Exception as err_msg:
			print ("Error in connecting the server")
			sys.exit(0)

	

def main(host, port):
	""" Main programm which will send the data to server 
	"""

	climate = Climate()
	climate.get_city()

	client = Client(host,port)
	sock = client.connect_server()

	while True:
		try:
			sock.send(climate.take_temperature())
			time.sleep(.5)
		except socket.error as e:
			print ("Server shutdown without notice")
			sys.exit(0)
		except KeyboardInterrupt as err_msg:
			print ("Client is going down")
			sys.exit(0)	
			
if __name__ == "__main__":
	host = "127.0.0.1"
	port = 53000
	main(host, port)
