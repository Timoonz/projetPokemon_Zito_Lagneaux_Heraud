from GUI_Combat import *
from POKEMON import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtGui import QPixmap
from GUI_Choix_pokemon import *
from Extraction_des_donnes import *




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
        self.update()
        
    def fuite(self):
        print("Vous prenez la fuite !")
        self.close()
        
    def attaque_neutre(self) :
        
        
        degats = int(pokemon2.attaque_neutre(pokemon1))
        pokemon1.hp -= degats
        print(pokemon1.hp)
        
        if pokemon1.hp <= 0 :
            pokemon1.hp = 0
            pokemon1.position = [-10,-10]
            pokemon1.hp = pokemon1.hp_init
            joueur.inventaire.append(pokemon1)
            Pokemon_sauvage.remove(pokemon1)
            self.close()
        
        else :
            degats = int(pokemon1.attaque_neutre(pokemon2))
            joueur.pokemon_choisi.hp -= degats
            print(joueur.pokemon_choisi.hp)
            
        if joueur.pokemon_choisi.hp<= 0 :
            joueur.pokemon_choisi.hp = 0
            
        self.update()   
        
    def attaque_speciale(self) :
        degats = int(pokemon2.attaque_speciale(pokemon1))
        pokemon1.hp -= degats
        print(pokemon1.hp)
        
        if pokemon1.hp <= 0 :
            pokemon1.hp = 0
            pokemon1.position = [-10,-10]
            pokemon1.hp = pokemon1.hp_init
            joueur.inventaire.append(pokemon1)
            Pokemon_sauvage.remove(pokemon1)
            self.close()
        
        else :
            degats = int(pokemon1.attaque_speciale(pokemon2))
            joueur.pokemon_choisi.hp -= degats
            print(joueur.pokemon_choisi.hp)  
        
        if joueur.pokemon_choisi.hp<= 0 :
            joueur.pokemon_choisi.hp = 0
            
        self.update()
        
    def update(self):
        image_path = "../Sprites_Pokemons/" + joueur.pokemon_choisi.name.lower() + "_Dos.png"
        pixmap = QPixmap(image_path)
        self.Pokemon_dos.setPixmap(pixmap)
        self.Pokemon_Dos_Nom.setText(joueur.pokemon_choisi.name)
        self.Pokemon_Dos_HP.setText( "HP " + str(joueur.pokemon_choisi.hp) + "/" + str(joueur.pokemon_choisi.hp_init))
        self.Pokemon_Face_HP.setText( "HP " + str(pokemon1.hp) + "/" + str(pokemon1.hp_init))
        
class Choix(QDialog):
    
    
    def __init__(self, parent=None):
        
            super(Choix, self).__init__(parent)
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)

    def accept(self):
        pokemon = self.ui.Liste_pokemons.selectedItems()[0].text()
        for i in joueur.inventaire : 
            if pokemon == i.name :
                joueur.pokemon_choisi = i
        print(joueur.pokemon_choisi)
        super().accept()

    

def Run_app():
        app = QApplication(sys.argv)
        mainWin = Combat()
        mainWin.show()
        app.exec_()
        
        






if __name__ == "__main__":
    # def run_app():
    #     app = QApplication(sys.argv)
    #     mainWin = Window()
    #     mainWin.show()
    #     app.exec_()
    Run_app()
    
    
    

