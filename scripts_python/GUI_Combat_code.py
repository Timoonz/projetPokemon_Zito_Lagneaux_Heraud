import random as rd
import time
from GUI_Combat import *
from POKEMON import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtGui import QPixmap
from GUI_Choix_pokemon import *
from Extraction_des_donnes import *

ko = 0

def attaque_ennemi(pokemon_sauvage, pokemon_choisi) :
    
    CM = pokemon_sauvage.faiblesses[pokemon_choisi.type_pokemon()]
    
    if CM == 2 :
        return pokemon_sauvage.attaque_speciale(pokemon_choisi)
    elif CM == 0.5 :
        return pokemon_sauvage.attaque_neutre(pokemon_choisi)
    else :
        alea = rd.randint(0,1)
        
        if alea == 0 :
            return pokemon_sauvage.attaque_speciale(pokemon_choisi)
        else :
            return pokemon_sauvage.attaque_neutre(pokemon_choisi)
        
class Combat(QMainWindow, Ui_MainWindow):
    
    
    def __init__(self, parent=None):
        
            super(Combat, self).__init__(parent)
            self.setupUi(self)
            
            # On assigne à chaque bouton de l'interface la fonction qui correspond
            self.att_neutre_bouton.clicked.connect(self.attaque_neutre)
            self.Att_sp_bouton.clicked.connect(self.attaque_speciale)
            self.fuite_bouton.clicked.connect(self.fuite)
            self.Chgt_pokemon_bouton.clicked.connect(self.Chgt_pokemon)
            
            
    def Chgt_pokemon(self):
        
        #Le test permet de savoir si tous les pokemons du joueurs sont ko
        if ko == len(joueur.inventaire) :
            
            self.textBrowser.setText("Tous vos pokemons sont ko, vous avez perdu le combat !")
            
            time.sleep(1)
            
            self.close()
        else :
            
            # dlg est la boite de dialogue utilisée pour changer de pokemon
            dlg = Choix(self)
            dlg.exec()
            
            # Nous avons décidé que changer de pokemon était une action au meme titre qu'attaquer donc après le changement, 
            # le nouveau pokemon subit des degats
            degats = attaque_ennemi(joueur.pokemon_adverse, joueur.pokemon_choisi)
            
            # On met à jour la barre d'hp, l'affichage des hp et on envoie un message indiquant
            # quel est le pokemon envoyé au combat
            self.barre_hp_choisi.setValue(int((joueur.pokemon_choisi.hp-degats)*100/joueur.pokemon_choisi.hp))
            joueur.pokemon_choisi.hp -= degats
            self.textBrowser.setText(joueur.pokemon_choisi.name + " est envoyé au combat !")       
            self.update()
        
    def fuite(self):
        
        global ko
        
        # Quand on fuit on récupère tous nos pokemons donc plus aucun n'est ko
        self.textBrowser.setText("Vous prenez la fuite !")
        ko = 0
        # time.sleep(1)
        
        self.close()
        
        
    def attaque_neutre(self) :
        
        global ko
        
        # Le pokemon choisi lance l'attaque neutre définie dans la classe Pokemon
        degats = joueur.pokemon_choisi.attaque_neutre(joueur.detecter(Pokemon_sauvage)[1])
        self.textBrowser.setText(joueur.pokemon_choisi.name + " utilise une attaque neutre")
        
        
        time.sleep(1)
        
        # On met à jour l'affichage 
        self.barre_hp_adverse.setValue(int((joueur.pokemon_adverse.hp-degats)*100/joueur.pokemon_adverse.hp))
        self.textBrowser.setText(joueur.pokemon_adverse.name + " a perdu " + str(degats) + " points de vie")
        joueur.pokemon_adverse.hp -= degats
        self.update()
        
        if joueur.pokemon_adverse.hp <= 0 :
            joueur.pokemon_adverse.hp = 0
            self.barre_hp_adverse.setValue(0)
            self.textBrowser.setText(joueur.pokemon_adverse.name + " a été capturé avec succès !")
            joueur.pokemon_adverse.position = [-10,-10]
            joueur.pokemon_adverse.hp = joueur.pokemon_adverse.hp_init
            joueur.inventaire.append(joueur.pokemon_adverse)
            Pokemon_sauvage.remove(joueur.pokemon_adverse)
            ko = 0
            self.close()
        
        else :
            time.sleep(1)
            degats = attaque_ennemi(joueur.pokemon_adverse, joueur.pokemon_choisi)
            self.textBrowser.setText(joueur.pokemon_adverse.name + " lance une attaque spéciale")
            time.sleep(1)
            self.barre_hp_choisi.setValue(int((joueur.pokemon_choisi.hp-degats)*100/joueur.pokemon_choisi.hp))
            self.textBrowser.setText(joueur.pokemon_choisi.name + " a perdu " + str(degats) + " points de vie")
            joueur.pokemon_choisi.hp -= degats
            
        if joueur.pokemon_choisi.hp<= 0 :
            joueur.pokemon_choisi.hp = 0
            self.barre_hp_choisi.setValue(0)
            self.textBrowser.setText(joueur.pokemon_choisi.name + " a été mis hors combat !")
            ko += 1
            self.update()
            self.Chgt_pokemon()
            
            
        self.update()   
        
    def attaque_speciale(self) :
        
        global ko
        
        degats = joueur.pokemon_choisi.attaque_speciale(joueur.pokemon_adverse)
        self.textBrowser.setText(joueur.pokemon_choisi.name + " lance une attaque spéciale")
        self.barre_hp_adverse.setValue(int((joueur.pokemon_adverse.hp-degats)*100/joueur.pokemon_adverse.hp))
        self.textBrowser.setText(joueur.pokemon_adverse.name + " a perdu " + str(degats) + " points de vie")
        joueur.pokemon_adverse.hp -= degats
        
        if joueur.pokemon_adverse.hp <= 0 :
            joueur.pokemon_adverse.hp = 0
            self.barre_hp_adverse.setValue(0)
            self.textBrowser.setText(joueur.pokemon_adverse.name + " a été capturé avec succès !")
            joueur.pokemon_adverse.position = [-10,-10]
            joueur.pokemon_adverse.hp = joueur.pokemon_adverse.hp_init
            joueur.inventaire.append(joueur.pokemon_adverse)
            Pokemon_sauvage.remove(joueur.pokemon_adverse)
            ko = 0
            self.close()
        
        else :
            time.sleep(1)
            degats = attaque_ennemi(joueur.pokemon_adverse, joueur.pokemon_choisi)
            self.textBrowser.setText(joueur.pokemon_adverse.name + " utilise une attaque neutre")
            self.barre_hp_choisi.setValue(int((joueur.pokemon_choisi.hp-degats)*100/joueur.pokemon_choisi.hp))
            self.textBrowser.setText(joueur.pokemon_choisi.name + " a perdu " + str(degats) + " points de vie")
            joueur.pokemon_choisi.hp -= degats
        
        if joueur.pokemon_choisi.hp<= 0 :
            joueur.pokemon_choisi.hp = 0
            self.barre_hp_choisi.setValue(0)
            self.textBrowser.setText(joueur.pokemon_choisi.name + " a été mis hors combat !")
            ko += 1
            self.update()
            self.Chgt_pokemon()
            
            
            
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
        
    def reset_hp(self):
        for i in joueur.inventaire:
            i.hp = i.hp_init
        
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
    
    
    

