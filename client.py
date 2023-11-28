import socket

def start_client():
    server_address = ('localhost', 5000)

    # Create a socket to connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect(server_address)
        print("Connected to {}:{}".format(*server_address))

        # Send data to the server
        message = "Hello, server! This is the client."
        client_socket.sendall(message.encode())
        print("Data sent to the server.")

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    start_client()
