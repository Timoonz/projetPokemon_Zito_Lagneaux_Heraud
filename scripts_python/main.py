# Importations

from MapAndSprite import Map, PlayerSprite

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import GUI_Combat_code as combat
import Extraction_des_donnes as data
from  PyQt5.QtTest import QTest
import Inventory as inv
import POKEMON as pk

# Game

class Game(QMainWindow) :
    
    def __init__(self) : 
        QMainWindow.__init__(self)
        self.setEnabled(True)
        self.fight = None
        
    def keyReleaseEvent(self, event) : 
        
        '''
        Cette fonction permet d'associer des touches du clavier à des fonctions/méthodes
        '''
        
        # On associe les flèches aux déplacements du joueur
        
        if event.key() == Qt.Key_Up and not event.isAutoRepeat():
            self.map.move("up")
            if pk.joueur.detecter(data.Pokemon_sauvage)[0]:
                self.open_fight()
                
                
        if event.key() == Qt.Key_Down and not event.isAutoRepeat(): 
            self.map.move("down")
            if pk.joueur.detecter(data.Pokemon_sauvage)[0]:
                self.open_fight()
                
                
        if event.key() == Qt.Key_Left and not event.isAutoRepeat(): 
            self.map.move("left")
            if pk.joueur.detecter(data.Pokemon_sauvage)[0]:
                self.open_fight()
                
                
        if event.key() == Qt.Key_Right and not event.isAutoRepeat(): 
            self.map.move("right")
            if pk.joueur.detecter(data.Pokemon_sauvage)[0]:
                self.open_fight()
        
        # Association de la touche i à l'ouverture de l'inventaire
        if event.key() == Qt.Key_I :
            self.open_inventory()
            
        # Association de la touche c à la méthode chanter 
        if event.key() == Qt.Key_C :
            pk.joueur.chanter()
            
        
        ##Processus qui nous a permis de faire la carte des collisions 
        
        # if event.key() == Qt.Key_H :
        #     j_p = str(joueur.position)
        #     Bloque_h.append(eval(j_p))
        #     print(j_p)
        #     print(Bloque_h)
            
        # if event.key() == Qt.Key_B :
        #     j_p = str(joueur.position)
        #     Bloque_b.append(eval(j_p))
        #     print(j_p)
        #     print(Bloque_b)
        
        # if event.key() == Qt.Key_G :
        #     j_p = str(joueur.position)
        #     Bloque_g.append(eval(j_p))
        #     print(j_p)
        #     print(Bloque_g)
        
        # if event.key() == Qt.Key_D :
        #     j_p = str(joueur.position)
        #     Bloque_d.append(eval(j_p))
        #     print(j_p)
        #     print(Bloque_d)
                
                
    
    def setupUi(self) : 
         
        #Initialisation de la fenêtre de jeu 
        self.resize(500, 500)
        self.setWindowTitle("Pokéming")
        
        #Ajout de la carte et du sprite du perso principal
        self.map = Map(self, "../sprites_ow/Map_finale.png")
        self.player = PlayerSprite(self, "../sprites_ow/player_ow_standing.png")
       
        
        
    def open_fight(self):
        
        '''
        Cette fonction permet d'ouvrir le combat entre le pokemon du jouer et le pokemon détecté
        '''
        
        pk.joueur.pokemon_adverse = pk.joueur.detecter(data.Pokemon_sauvage)[1]
        self.fight = combat.Combat()
        self.fight.barre_hp_adverse.setValue(100)
        self.fight.barre_hp_choisi.setValue(100)
        self.fight.reset_hp()
        self.fight.update()
        self.fight.textBrowser.setText("Un " + pk.joueur.pokemon_adverse.name + " est apparu !")        
        self.fight.show()
        QTest.qWait(2000)
        self.fight.textBrowser.setText("C'est un pokemon de type " + pk.joueur.pokemon_adverse.type_pokemon() + ".")
        
        
    def open_inventory(self):
        
        '''
        Cette fonction permet d'ouvrir la fenêtre de l'inventaire
        '''
        
        # Crée une fenêtre secondaire avec un ListWidget qui fait figure d'inventaire
        self.inventory = inv.Ui_Inventory()
        self.inventory.show()
        
        
    
if __name__ == "__main__" : 
    def run_app() : 
        app = QtWidgets.QApplication(sys.argv)
        game = Game()
        game.setupUi()
        game.show()
        sys.exit(app.exec_())
        
    run_app()