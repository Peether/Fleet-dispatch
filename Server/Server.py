from ipaddress import ip_address
import yaml
import socket
import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    
)  

with open('serveconfig.yaml', 'r') as file:
serverSettings = yaml.full_load(file)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(serverSettings['IP']['PORT'])
