from GUI_Combat import *
from POKEMON import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from GUI_Choix_pokemon import *





class Combat(QMainWindow, Ui_MainWindow):
    
    
    def __init__(self, parent=None):
        
            super(Combat, self).__init__(parent)
            self.setupUi(self)
            # self.att_neutre_bouton.clicked.connect(joueur.choisir_un_pokemon().attaque_neutre())
            # self.att_sp_bouton.clicked.connect(joueur.choisir_un_pokemon.attaque_speciale())
            self.fuite_bouton.clicked.connect(self.fuite)
            self.Chgt_pokemon_bouton.clicked.connect(self.Chgt_pokemon)
            
            
    def Chgt_pokemon(self):
        dlg = Choix(self)
        dlg.exec()
        
    def fuite(self):
        self.close()

class Choix(QDialog):
    
    
    def __init__(self, parent=None):
        
            super(Choix, self).__init__(parent)
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)

    # def accept(self):
    #     crsTxt = self.ui.crs.text()
    #     self.parent().Liste_pokemons.addItem(crsTxt)
    #     super().accept()

    

def run_app():
        app = QApplication(sys.argv)
        mainWin = Combat()
        mainWin.show()
        app.exec_()
        
        

# if joueur.detecter() == True:
#     run_app()





if __name__ == "__main__":
    # def run_app():
    #     app = QApplication(sys.argv)
    #     mainWin = Window()
    #     mainWin.show()
    #     app.exec_()
    run_app()
    
    
    

