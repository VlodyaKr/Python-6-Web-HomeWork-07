import socket

_HOST = '192.168.17.176'
_PORT = 5000
_BUFFER_SIZE = 1024


def client():
    with socket.socket() as client_socket:
        client_socket.connect((_HOST, _PORT))
        message = input('Please input message --> ')

        while message.lower().strip() != 'end':
            client_socket.send(message.encode())
            data = client_socket.recv(_BUFFER_SIZE).decode()
            print(f'Received message: {data}')

            message = input('Please input message --> ')


if __name__ == '__main__':
    client()
