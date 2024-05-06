from GUI_Combat import *
from POKEMON import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
            super(Window, self).__init__(parent)
            self.setupUi(self)
            # self.att_neutre_bouton.clicked.connect(attaque_neutre())




if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = Window()
        mainWin.show()
        app.exec_()
    run_app()

