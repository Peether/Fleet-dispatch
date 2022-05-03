import sys
from tkinter import Menu

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar



class guiClient(QMainWindow): #Main gui window
    
    def __init__(self, parent=None): #Initializer
        
        super().__init__(parent)
        self.setWindowTitle("UltimateGUI")
        self.setCentralWidget(QLabel("I am your central widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
    
    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)
        
    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('&Exit', self.close)
                
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I am status bar")
        self.setStatusBar(status)
    
     
if __name__=="__main__":
        app = QApplication(sys.argv)
        win = guiClient()
        win.show()
        sys.exit(app.exec_())
