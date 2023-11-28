import socket
import ipaddress

class SimpleFirewall:
    def __init__(self):
        # Define allowed IP addresses
        self.allowed_ips = [
            "127.0.0.1",  # localhost
            "192.168.1.100",  # example allowed IP
        ]

    def is_allowed(self, client_ip):
        # Check if the client's IP is in the list of allowed IPs
        return client_ip in self.allowed_ips

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 5000)

        # Bind the server to the specified address and port
        server_socket.bind(server_address)

        # Listen for incoming connections
        server_socket.listen(1)
        print("Server is listening on {}:{}".format(*server_address))

        while True:
            # Wait for a connection
            print("Waiting for a connection...")
            client_socket, client_address = server_socket.accept()
            print("Accepted connection from {}:{}".format(*client_address))

            # Check firewall rule before processing the connection
            if self.is_allowed(client_address[0]):
                self.handle_connection(client_socket, client_address[0], server_address[0])
            else:
                print("Connection from {} blocked by firewall.".format(client_address[0]))
                client_socket.close()

    def handle_connection(self, client_socket, client_ip, server_ip):
        # Print packet route
        print("Packet Route: {} -> {}".format(client_ip, server_ip))

        # Handle the connection (e.g., send/receive data)
        data = client_socket.recv(1024)
        print("Received data: {}".format(data.decode()))

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    firewall = SimpleFirewall()
    firewall.start_server()
