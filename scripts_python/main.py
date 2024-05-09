# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:32:26 2024

@author: timot
"""
from MapAndSprite import Map, Player

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap

class Game(QMainWindow) :
    def __init__(self) : 
        QMainWindow.__init__(self)
        self.setEnabled(True)
        
    def keyReleaseEvent(self, event) : 
        if event.key() == Qt.Key_Up :
            self.map.move("up")
            self.player.sprite.setPixmap(QPixmap("player_ow_up.png"))
        if event.key() == Qt.Key_Down : 
            self.map.move("down")
        if event.key() == Qt.Key_Left : 
            self.map.move("left")
        if event.key() == Qt.Key_Right : 
            self.map.move("right")
    
    def setupUi(self) : 
         
        #Initialisation de la fenêtre de jeu 
        self.resize(500, 500)
        self.setWindowTitle("Pokéming")
        
        #Ajout de la carte et du sprite du perso principal
        self.map = Map(self, "map_abi.jpeg")
        self.player = Player(self, "player_ow_standing.png")
        
        
     
        
        
        
    
if __name__ == "__main__" : 
    def run_app() : 
        app = QtWidgets.QApplication(sys.argv)
        game = Game()
        game.setupUi()
        game.show()
        sys.exit(app.exec_())
        
    run_app()