import sys
from PyQt5.QtWidgets import QApplication,QWidget

class F(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        self.setGeometry(100,100,600,600)
        self.setWindowTitle("application title")
        self.show()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec_())