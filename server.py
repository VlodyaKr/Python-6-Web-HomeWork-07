import concurrent.futures
import socket

_HOST = ''
_PORT = 5000
_MAX_CONNECTION = 3
_BUFFER_SIZE = 1024


def connection_handler(conn: socket.socket, address: str):
    print(f'Connection from {address}')
    while True:
        data = conn.recv(_BUFFER_SIZE).decode()
        if not data:
            break
        print(f'From {address} received message: {data}')
        message = 'OK'
        conn.send(message.encode())
    print(f'Socket connection from {address} closed!')
    conn.close()


def server():
    with socket.socket() as server_socket:
        server_socket.bind((_HOST, _PORT))
        server_socket.listen(_MAX_CONNECTION)
        print(f'Start server {socket.gethostname()}')
        with concurrent.futures.ThreadPoolExecutor(_MAX_CONNECTION) as client_pool:
            try:
                while True:
                    conn, address = server_socket.accept()
                    client_pool.submit(connection_handler, conn, address)
            except KeyboardInterrupt:
                print(f'Server {socket.gethostname()} finished!')


if __name__ == '__main__':
    server()
