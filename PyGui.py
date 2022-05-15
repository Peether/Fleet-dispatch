
import sys
from PyQt5.QtCore import Qt
import PyGui 
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QToolBar,
    QToolButton,
    QMenu
    
)

#GUI:n pääikkuna
class guiClient(QMainWindow): 
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Fleet Command")
        
        #Central widget on pää ikkunan oma layout, Ei tarvita erillistä layoptuttia. 
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._createmenu()
        self._createtoolbar()
        self._createactions()
        
        
    def _createmenu(self):
        menuBar = self.menuBar()
        menuNames = ["&File", "&Tools", "&Help", self]
        #File valikko   
        fileMenu = QMenu(menuNames[0], self)
        menuBar.addMenu(fileMenu)
        #Tools valikko
        toolsMenu = QMenu(menuNames[1],self)
        menuBar.addMenu(toolsMenu)
        #Help valikko
        helpMenu = QMenu(menuNames[2],self)
        menuBar.addMenu(helpMenu)
    
    def _createtoolbar(self):
        toolBar = self.addToolBar("Tools")
        toolBar.setMovable(True)
        
        pass
        
        
    def _createactions(self):
        pass
     
if __name__=="__main__":
        app = QApplication(sys.argv)
        win = guiClient()
        win.showMaximized()
        win.show()
        sys.exit(app.exec_())
