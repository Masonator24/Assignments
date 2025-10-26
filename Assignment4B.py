# Program Name: Assignment4A.py (use the name the program is saved as)
	# Course: IT3883/Section W02
	# Student Name: Mason Gilbert
	# Assignment Number: Assignment 4
	# Due Date: 10/26/2025
	# Purpose: This program allows for users to send a string to a connected server. It will then be sent and converted into upper case and shall be sent back to the user.
  # List Specific resources used to complete the assignment. (PyCharm as an IDE), Stackflow, Baeldung, Python.org, KSU Slideshows
import socket
#These are the server details
server_host = "127.0.0.1"
port = 40121
#This creates a server to be used for receiving and connect with program A
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind((server_host, port))
socket_server.listen(1)
print(f"Server is currently listening on {server_host}:{port}!")
connection, address = socket_server.accept()
print("Successfully connected!")

data = connection.recv(1024)
#The string will then be converted into uppercase and then sent back to program A before closing
server_response = data.decode().upper()
connection.sendall(server_response.encode())
print("The message has been converted and sent back!")

connection.close()
socket_server.close()
