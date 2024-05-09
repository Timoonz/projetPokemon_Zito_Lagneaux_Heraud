# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:38:04 2024

@author: timot
"""

class Deplacement() : 
    
    def __init__(self, mainWindow) : 
        self.player = mainWindow.player
        self.map = mainWindow.map
        
        
    def move(self, direction) : 
        
        pos = self.map.map.geometry()
        
        if direction == "up" :
            pos.translate(0, 50)
            
        if direction == "down" :
            pos.translate(0, -50)
            
        if direction == "left" :
            pos.translate(-50, 0)
            
        if direction == "right" :
            pos.translate(50, 0)