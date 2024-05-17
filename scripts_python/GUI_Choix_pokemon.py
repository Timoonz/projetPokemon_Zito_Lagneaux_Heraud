# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choix_pokemon.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from POKEMON import joueur


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Liste_pokemons = QtWidgets.QListWidget(Dialog)
        self.Liste_pokemons.setObjectName("Liste_pokemons")
        item = QtWidgets.QListWidgetItem()
        self.Liste_pokemons.addItem(item)
        self.gridLayout.addWidget(self.Liste_pokemons, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Liste_De_Pokemons"))
        __sortingEnabled = self.Liste_pokemons.isSortingEnabled()
        self.Liste_pokemons.setSortingEnabled(False)
        # item = self.Liste_pokemons.item(0)
        # item.setText(_translate("Dialog", "Charmander"))
        
        for i in range(len(joueur.inventaire)):
            itemm = QtWidgets.QListWidgetItem()
            self.Liste_pokemons.addItem(itemm)
            item = self.Liste_pokemons.item(i+1)
            if joueur.inventaire[i].isKo :
                item.setText(_translate("Dialog",joueur.inventaire[i].name + ' (K.O.) '))
            else :
                item.setText(_translate("Dialog",joueur.inventaire[i].name))
        
        
        
        
        self.Liste_pokemons.setSortingEnabled(__sortingEnabled)
