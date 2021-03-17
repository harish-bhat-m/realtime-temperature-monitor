# realtime-temperature-monitor
Python socket based clinets-server program. Server collects and displays the temperature gauge verious clients

## Description:
This is simplest implementation of client and server architecture which uses the plain
sockets for the communication between client and server. Server makes use of the threading
mechanism, where depending on the client instances, the new threads are created.

## Requirement
Python 3.5 and +

## How to run:
1. Run the server.py using "python server.py". As soon as you start the server, the server 
   displayes the message "Server Started"

2. Run the client.py using "python client.py". The client will ask for the City name to be 
   entered by the user. As soon as you city name is entered. The client will start to gauge 
   the temperature and prints the value for each second.

3. As soon as client starts to print the temperature details, it aslo sends the details to 
   the server and server starts to display the city name and temperature.

4. You can run the multiple client.py with different city name as an input.
   Based on the client running, the server shows the multiple city temperature reading in realtime. 
