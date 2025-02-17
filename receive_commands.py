import socket

def start_server(host='0.0.0.0', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    command = data.decode('utf-8')
                    print(f"Received command: {command}")
                    
                    # Process the command (replace with our actual command handling)
                    response = f"Executing command: {command}"
                    
                    conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()