# Program Name: Assignment4A.py (use the name the program is saved as)
	# Course: IT3883/Section W02
	# Student Name: Mason Gilbert
	# Assignment Number: Assignment 4
	# Due Date: 10/26/2025
	# Purpose: This program allows for users to send a string to a connected server. It will then be sent and converted into upper case and shall be sent back to the user.
  # List Specific resources used to complete the assignment. (PyCharm as an IDE), Stackflow, Baeldung, Python.org, KSU Slideshows

import socket
#These are the details for the server
server_ip = "127.0.0.1"
port = 40021
#This will create a socket to be used
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to server at {server_ip}:{port}")
socket_client.connect((server_ip, port))
print("Successful Connection!")
#The user will then be asked to input a string
user_input = input("Please enter a string to send: ")
#The string is sent to the converter server and wait for its response
socket_client.sendall(user_input.encode())
server_response = socket_client.recv(1024).decode()
#The response is received and the connection is closed
print("Response received from server!", server_response)
socket_client.close()
