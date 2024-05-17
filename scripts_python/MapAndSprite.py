# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:31:09 2024

@author: timot
"""

#from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import POKEMON as pk

class Map() : 
    
    def __init__(self, mainWindow, mapPath) : 
        self.map = QLabel(mainWindow)
        self.map.setGeometry(QtCore.QRect(-75, -25, 2000, 2000))
        self.map.setText("")
        self.map.setScaledContents(True)
        self.map.setObjectName("map")
        self.map.setPixmap(QPixmap(mapPath))
        self.mainWindow = mainWindow
        
        
    def move(self, direction) : 
        pos = self.map.geometry()
        
        if direction == "up" and pk.joueur.position[1] < 3.5:
            pos.translate(0, 25)
            pk.joueur.position[1] += 0.5
            
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("../sprites_ow/player_ow_up.png"))
            
        if direction == "down" and pk.joueur.position[1] > -29.5:
            pos.translate(0, -25)
            pk.joueur.position[1] -= 0.5
            
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("../sprites_ow/player_ow_down.png"))
            
        if direction == "left" and pk.joueur.position[0]>-1 :
            pos.translate(25, 0)
            pk.joueur.position[0] -= 0.5
            
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("../sprites_ow/player_ow_left.png"))
            
        if direction == "right" and pk.joueur.position[0] < 27.5:
            pos.translate(-25, 0)
            pk.joueur.position[0] += 0.5
            
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("../sprites_ow/player_ow_right.png"))
            
       
class PlayerSprite() : 
    
    def __init__(self, mainWindow, spritePath) :
        self.sprite = QLabel(mainWindow)
        self.sprite.setGeometry(250, 250, 50, 50)
        self.sprite.setText("")
        self.sprite.setScaledContents(True)
        self.sprite.setPixmap(QPixmap(spritePath))
        self.sprite.setObjectName("player")
        