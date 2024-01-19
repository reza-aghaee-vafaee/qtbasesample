import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class F(QWidget):
    def __init__(self) :
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(100,100,600,600)
        self.setWindowTitle("push button")
        self.btn = QPushButton("click me",self)
        self.btn.move(100,100)
        self.show()
        self.btn.clicked.connect(self.click)
        self.btn.clicked.connect(self.click2)
    def click(self):
        print("button clicked")
    def click2(self):
        print("button clicked 2")
        #self.close()
if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec_())