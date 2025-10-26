import socket
server_ip = "127.0.0.1"
port = 40021
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to server at {server_ip}:{port}")
socket_client.connect((server_ip, port))
print("Successful Connection!")
user_input = input("Please enter a string to send: ")
socket_client.sendall(user_input.encode())
server_response = socket_client.recv(1024).decode()
print("Response received from server!")
socket_client.close()
