from GUI_Combat import *
from POKEMON import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from GUI_Choix_pokemon import *


pokemon2 = joueur.inventaire[2]


class Combat(QMainWindow, Ui_MainWindow):
    
    
    def __init__(self, parent=None):
        
            super(Combat, self).__init__(parent)
            self.setupUi(self)
            self.att_neutre_bouton.clicked.connect(self.attaque_neutre)
            self.Att_sp_bouton.clicked.connect(self.attaque_speciale)
            self.fuite_bouton.clicked.connect(self.fuite)
            self.Chgt_pokemon_bouton.clicked.connect(self.Chgt_pokemon)
            
            
    def Chgt_pokemon(self):
        dlg = Choix(self)
        dlg.exec()
        
    def fuite(self):
        print("Vous prenez la fuite !")
        self.close()
        
    def attaque_neutre(self) :
        
        degats = pokemon2.attaque_neutre(pokemon1)
        pokemon1.hp -= degats
        print(pokemon1.hp)
        
        if pokemon1.hp <= 0 :
            pokemon1.position = [-10,-10]
            joueur.inventaire.append(pokemon1)
            print(joueur.inventaire)
            Pokemon_sauvage.remove(pokemon1)
        
        else :
            degats = pokemon1.attaque_neutre(pokemon2)
            pokemon2.hp -= degats
            print(pokemon2.hp)
            
        
    def attaque_speciale(self) :
        degats = pokemon2.attaque_speciale(pokemon1)
        pokemon1.hp -= degats
        print(pokemon1.hp)
        
        if pokemon1.hp <= 0 :
            pokemon1.position = [-10,-10]
            joueur.inventaire.append(pokemon1)
            print(joueur.inventaire)
            Pokemon_sauvage.remove(pokemon1)
        
        else :
            degats = pokemon1.attaque_speciale(pokemon2)
            pokemon2.hp -= degats
            print(pokemon2.hp)        
            

class Choix(QDialog):
    
    
    def __init__(self, parent=None):
        
            super(Choix, self).__init__(parent)
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)

    def accept(self):
        pokemon2 = self.ui.Liste_pokemons.selectedItems()[0].text()
        # joueur.inventaire.append(crsTxt)
        print(pokemon2)
        super().accept()

    

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
    
    
    

