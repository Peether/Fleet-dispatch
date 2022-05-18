import threading
import socket

HOST = ('Localhost')
PORT = 9090
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(HOST, PORT)

