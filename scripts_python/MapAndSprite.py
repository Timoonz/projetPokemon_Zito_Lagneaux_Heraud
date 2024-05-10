# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:31:09 2024

@author: timot
"""

#from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class Map() : 
    
    def __init__(self, mainWindow, mapPath) : 
        self.map = QLabel(mainWindow)
        self.map.setGeometry(QtCore.QRect(0, 0, 2000, 500))
        self.map.setText("")
        self.map.setScaledContents(True)
        self.map.setObjectName("map")
        self.map.setPixmap(QPixmap(mapPath))
        self.mainWindow = mainWindow
        
    def move(self, direction) : 
        pos = self.map.geometry()
        
        if direction == "up" :
            pos.translate(0, 50)
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("player_ow_up.png"))
            
        if direction == "down" :
            pos.translate(0, -50)
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("player_ow_down.png"))
            
        if direction == "left" :
            pos.translate(50, 0)
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("player_ow_left.png"))
            
        if direction == "right" :
            pos.translate(-50, 0)
            self.map.setGeometry(pos)
            self.mainWindow.player.sprite.setPixmap(QPixmap("player_ow_right.png"))
        
class Player() : 
    
    def __init__(self, mainWindow, spritePath) :
        self.sprite = QLabel(mainWindow)
        self.sprite.setGeometry(250, 250, 50, 50)
        self.sprite.setText("")
        self.sprite.setScaledContents(True)
        self.sprite.setPixmap(QPixmap(spritePath))
        self.sprite.setObjectName("player")
        