import socket
from typing import Tuple
import threading

def handle_client(connection: socket.socket, address: Tuple[str, int]) -> None:
    with connection:
        print(f"Accepted connection from {address}\n")
        while True:
            data: bytes = connection.recv(1024)
            if not data:
                print(f"Connection closed by {address}")
                break
            if "ping" in data.decode().lower():
                pong: str = "+PONG\r\n"
                connection.sendall(pong.encode())
            else:
                # Handle other commands or provide a default response
                response: str = "+OK\r\n"
                connection.sendall(response.encode())

def main() -> None:
    print("Logs from your program will appear here!\n")
    server_socket: socket.socket = socket.create_server(
        ("localhost", 6379), reuse_port=True
    )
    print("Server started on localhost:6379")

    while True:
        try:
            connection: socket.socket
            address: Tuple[str, int]
            connection, address = server_socket.accept()

            # Start a new thread for each client
            client_thread = threading.Thread(
                target=handle_client, args=(connection, address)
            )
            client_thread.start()
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    main()
