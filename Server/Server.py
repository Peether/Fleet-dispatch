from socket import socket
import sys, time
import socket
from socketserver import ThreadingMixIn
from threading import Thread
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

# Server gui mainlayout
conn = None
class serverMain(QMainWindow):

    def __init__(self,*args, **kwargs):
        super(serverMain, self).__init__(*args, **kwargs)
        mainLayout = QHBoxLayout()
        widget = QStackedWidget()
        widget.setLayout(mainLayout)
        mainWindow = QMainWindow()
        self.setWindowTitle("Fleetcom server")
        mainWindow.setWindowIcon(QtGui.QIcon(":window.png"))
        self.setStyleSheet("background-color: #404040;")
        self.setCentralWidget(widget)
        menuBar = self.menuBar()
        menuBar.setStyleSheet("background-color: lightGrey;")
        fileMenu = QMenu("&Tiedosto", self)
        menuBar.addMenu(fileMenu)
        toolsMenu = QMenu("&Työkalut", self)
        menuBar.addMenu(toolsMenu)        
                
        
# Messager layout       
class commWindow(QWidget):
    def __init__(self, parent=True):
        super(commWindow).__init__(self)
        
        
        
class serverConnection(Thread):
    
    def __init__(self,serverMain):
        thread.__init__(self)
        self.serverMain = serverMain
    
    def serverRun(self):
        TCP_IP = 'localhost'
        TCP_PORT = 9090
        BUFFER_SIZE = 20
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        tcpServer.bind((TCP_IP,TCP_PORT))
        threads = []
        nicknames =[]
        
        tcpServer.listen(5)
        while True
            print("Fleetcom server : Waiting for Client connections...")
            global conn
            (conn,(ip,port)) = tcpServer.accept()
            newConnection = ClientThread(ip,port,serverMain)
            newConnection.start()
            threads.append(newConnection)
            
            for t in threads:
                t.join()
                
        
    
    def recieve(self):
        pass
    
    def sending(self):
        pass
    
    def handler(self):
        pass  

           
           
           
           
if __name__ == '__main__':
    serverApp = QApplication(sys.argv)
    
    appWindow = serverMain()
    appWindow.show()
    appWindow.showMaximized()
    serverApp.exec_()
    
    sys.exit(serverApp.exec_())