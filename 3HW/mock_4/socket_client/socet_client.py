import socket
from time import sleep

from flask import request


class SocketClient:

    def __init__(self, target_host, target_port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.target_host = target_host
        self.target_port = target_port
        sleep(1)
        self.client.connect((self.target_host, self.target_port))

        
    def get_request(self, id_u):
        self.__init__(self.target_host, self.target_port)
        params = f"/user/{id_u}"
        get_request = f'GET {params} HTTP/1.1\r\nHost:{self.target_host}\r\n\r\n'
        self.client.send(get_request.encode())
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = ''.join(total_data).splitlines()
        return data

    def post_request(self, user, id_u):
        self.__init__(self.target_host, self.target_port)
        params = f"/user"
        data = f'id={str(id_u)}&name={user[str(id_u)]["name"]}&surname={user[str(id_u)]["surname"]}'
        post_request = f'POST {params} HTTP/1.1\r\nContent-Length:{len(data)}\r\n' \
                       f'Content-Type:application/x-www-form-urlencoded\r\n\r\n{data}'
        self.client.send(post_request.encode())

        total_data = []
        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = ''.join(total_data).splitlines()
        return data
