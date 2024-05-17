# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:32:26 2024

@author: timot
"""
from MapAndSprite import *

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QListWidget
from PyQt5.QtGui import QPixmap
from GUI_Combat_code import *
from Inventory import *


class Game(QMainWindow) :
    def __init__(self) : 
        QMainWindow.__init__(self)
        self.setEnabled(True)
        self.fight = None
        
    def keyReleaseEvent(self, event) : 
        if event.key() == Qt.Key_Up and not event.isAutoRepeat():
            self.map.move("up")
            if joueur.detecter(Pokemon_sauvage)[0]:
                
               
                self.open_fight()
                
                
        if event.key() == Qt.Key_Down and not event.isAutoRepeat(): 
            self.map.move("down")
            if joueur.detecter(Pokemon_sauvage)[0]:
                
                self.open_fight()
                
                
        if event.key() == Qt.Key_Left and not event.isAutoRepeat(): 
            self.map.move("left")
            if joueur.detecter(Pokemon_sauvage)[0]:
                
                self.open_fight()
                
                
        if event.key() == Qt.Key_Right and not event.isAutoRepeat(): 
            self.map.move("right")
            if joueur.detecter(Pokemon_sauvage)[0]:
                
                self.open_fight()
        
        if event.key() == Qt.Key_I :
            self.open_inventory()
            
        if event.key() == Qt.Key_H :
            j_p = str(joueur.position)
            Bloque_h.append(eval(j_p))
            print(j_p)
            print(Bloque_h)
            
        if event.key() == Qt.Key_B :
            j_p = str(joueur.position)
            Bloque_b.append(eval(j_p))
            print(j_p)
            print(Bloque_b)
        
        if event.key() == Qt.Key_G :
            j_p = str(joueur.position)
            Bloque_g.append(eval(j_p))
            print(j_p)
            print(Bloque_g)
        
        if event.key() == Qt.Key_D :
            j_p = str(joueur.position)
            Bloque_d.append(eval(j_p))
            print(j_p)
            print(Bloque_d)
                
                
    
    def setupUi(self) : 
         
        #Initialisation de la fenêtre de jeu 
        self.resize(500, 500)
        self.setWindowTitle("Pokéming")
        
        #Ajout de la carte et du sprite du perso principal
        self.map = Map(self, "../sprites_ow/Map_finale.png")
        self.player = Player(self, "../sprites_ow/player_ow_standing.png")
       
        
        
    def open_fight(self):
        
        
        joueur.pokemon_adverse = joueur.detecter(Pokemon_sauvage)[1]
        self.fight = Combat()
        self.fight.barre_hp_adverse.setValue(100)
        self.fight.barre_hp_choisi.setValue(100)
        self.fight.reset_hp()
        self.fight.update()
        self.fight.show()
        
        
    def open_inventory(self):
        # Crée une fenêtre secondaire avec un ListWidget
        self.inventory = Ui_Inventory()
        self.inventory.show()
        
        
        
    
if __name__ == "__main__" : 
    def run_app() : 
        app = QtWidgets.QApplication(sys.argv)
        game = Game()
        game.setupUi()
        game.show()
        sys.exit(app.exec_())
        
    run_app()