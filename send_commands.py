import socket

def send_command(command, ip_address='192.168.1.100', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        s.sendall(command.encode('utf-8'))
        data = s.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    while True:
        command = input("Enter command (or 'quit' to exit): ")
        if command.lower() == 'quit':
            break
        send_command(command)