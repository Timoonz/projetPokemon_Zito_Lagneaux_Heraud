# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from POKEMON import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QListWidget


    
class Ui_Inventory(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory")
        self.setGeometry(0, 0, 300, 200)


        self.Liste_pokemons = QListWidget()
        
        # On récupère les pokemons presents dans l'invenatire du joueur pour l'afficher dans la fenetre
        
        for i in range(len(joueur.inventaire)):
            self.Liste_pokemons.addItem(str(joueur.inventaire[i].name))

        layout = QVBoxLayout()
        layout.addWidget(self.Liste_pokemons)
        self.setLayout(layout)

