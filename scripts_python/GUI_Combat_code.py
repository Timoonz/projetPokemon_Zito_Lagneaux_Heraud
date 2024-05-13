from GUI_Combat import *
from POKEMON import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtGui import QPixmap
from GUI_Choix_pokemon import *
from Extraction_des_donnes import *

pokemon1 = joueur.detecter(Pokemon_sauvage)[1]


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
        
        
        degats = int(joueur.pokemon_choisi.attaque_neutre(joueur.detecter(Pokemon_sauvage)[1]))
        joueur.pokemon_adverse.hp -= degats
        print(joueur.pokemon_adverse.hp)
        
        if joueur.pokemon_adverse.hp <= 0 :
            joueur.pokemon_adverse.hp = 0
            joueur.pokemon_adverse.position = [-10,-10]
            joueur.pokemon_adverse.hp = joueur.pokemon_adverse.hp_init
            joueur.inventaire.append(joueur.pokemon_adverse)
            Pokemon_sauvage.remove(joueur.pokemon_adverse)
            self.close()
        
        else :
            degats = int(joueur.pokemon_adverse.attaque_neutre(joueur.pokemon_choisi))
            joueur.pokemon_choisi.hp -= degats
            print(joueur.pokemon_choisi.hp)
            
        if joueur.pokemon_choisi.hp<= 0 :
            joueur.pokemon_choisi.hp = 0
            self.close()
            
        self.update()   
        
    def attaque_speciale(self) :
        degats = int(joueur.pokemon_choisi.attaque_speciale(joueur.pokemon_adverse))
        joueur.pokemon_adverse.hp -= degats
        print(joueur.pokemon_adverse.hp)
        
        if joueur.pokemon_adverse.hp <= 0 :
            joueur.pokemon_adverse.hp = 0
            joueur.pokemon_adverse.position = [-10,-10]
            joueur.pokemon_adverse.hp = joueur.pokemon_adverse.hp_init
            joueur.inventaire.append(joueur.pokemon_adverse)
            Pokemon_sauvage.remove(joueur.pokemon_adverse)
            self.close()
        
        else :
            degats = int(joueur.pokemon_adverse.attaque_speciale(joueur.pokemon_choisi))
            joueur.pokemon_choisi.hp -= degats
            print(joueur.pokemon_choisi.hp)  
        
        if joueur.pokemon_choisi.hp<= 0 :
            joueur.pokemon_choisi.hp = 0
            self.close()
            
        self.update()
        
    def update(self):
        image_path = "../Sprites_Pokemons/" + joueur.pokemon_choisi.name.lower() + "_Dos.png"
        pixmap = QPixmap(image_path)
        image_path2 = "../Sprites_Pokemons/" + joueur.pokemon_adverse.name.lower() + "_Face.png"
        pixmap2 = QPixmap(image_path2)
        self.Pokemon_dos.setPixmap(pixmap)
        self.Poekmon_Face.setPixmap(pixmap2)
        self.Pokemon_Dos_Nom.setText(joueur.pokemon_choisi.name)
        self.Pokemon_Face_Nom.setText(joueur.pokemon_adverse.name)
        self.Pokemon_Dos_HP.setText( "HP " + str(joueur.pokemon_choisi.hp) + "/" + str(joueur.pokemon_choisi.hp_init))
        self.Pokemon_Face_HP.setText( "HP " + str(joueur.pokemon_adverse.hp) + "/" + str(joueur.pokemon_adverse.hp_init))
        
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
        # print(joueur.pokemon_choisi)
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
    
    
    

