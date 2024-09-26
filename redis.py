import socket
import threading


def redis_encode(data, encoding="utf-8"):
    if not isinstance(data, list):
        data = [data]
    
    separator = "\r\n"
    encoded = []
    

    for datum in data:
        encoded.append(f"${len(datum)}")
        encoded.append(datum)
    
    if len(data) > 1:
        encoded.insert(0, f"*{len(data)}")
    
    return (separator.join(encoded) + separator).encode(encoding)


def redis_decode(data):
    parts = data.split(b"\r\n")
    cmd = parts[2].decode("utf-8")
    if cmd.lower() == 'ping':
        return ['ping']
    elif cmd.lower() == 'echo':
        return ['echo', parts[4].decode("utf-8")]
    return None


def handle_connection(conn, addr):
    print(f"Connection from {addr}")
    
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            
            command = redis_decode(data)
            if not command:
                print("Invalid data received")
                break
            
            print(f"Received command: {command}")
            
            if command[0] == 'ping':
                resp = redis_encode("PONG")
            elif command[0] == 'echo':
                resp = redis_encode(command[1])
            else:
                resp = redis_encode("ERR unknown command")
            
            conn.sendall(resp)
    
    except Exception as e:
        print(f"Error with connection from {addr}: {e}")
    
    finally:
        conn.close()
        print(f"Connection closed from {addr}")

# Main server loop
def main():
    server = socket.create_server(("localhost", 6379))
    server.listen()
    print("Server is listening on localhost:6379")
    
    try:
        while True:
            conn, addr = server.accept()
            client_thread = threading.Thread(target=handle_connection, args=(conn, addr))
            client_thread.start()
    
    except KeyboardInterrupt:
        print("Server shutting down...")
    
    finally:
        server.close()

if __name__ == "__main__":
    main()
