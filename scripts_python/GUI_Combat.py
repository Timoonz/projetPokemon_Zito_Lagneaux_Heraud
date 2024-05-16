# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from POKEMON import *
from Extraction_des_donnes import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog , QProgressBar




pokemon2 = joueur.pokemon_choisi




class Choix(QDialog):
    
    
    def __init__(self, parent=None):
        
            super(Choix, self).__init__(parent)
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)

    # def accept(self):
        
    #     global pokemon2
        
    #     pokemon2 = self.ui.Liste_pokemons.selectedItems()[0].text()
    #     # joueur.inventaire.append(crsTxt)    
    #     print(pokemon2)
        
    #     QtGui.QApplication.processEvents()
    #     super().accept()
    #     print(pokemon2)
        
class ProgressBar(QProgressBar):
 
    def __init__(self, *args, **kwargs):
        super(ProgressBar, self).__init__(*args, **kwargs)
        self.setValue(100)
        
               
        
        
        
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 601)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.barre_hp_adverse = QProgressBar(self)
        self.barre_hp_adverse.setGeometry(350, 110, 100, 15)
        self.barre_hp_adverse.setValue(100)
        
        
        self.barre_hp_choisi = QProgressBar(self)
        self.barre_hp_choisi.setGeometry(100, 170, 100, 15)
        self.barre_hp_choisi.setValue(100)
        
        
        
        
        self.att_neutre_bouton = QtWidgets.QPushButton(self.centralwidget)
        self.att_neutre_bouton.setGeometry(QtCore.QRect(90, 310, 231, 101))
        self.att_neutre_bouton.setObjectName("att_neutre_bouton")
        self.Att_sp_bouton = QtWidgets.QPushButton(self.centralwidget)
        self.Att_sp_bouton.setGeometry(QtCore.QRect(440, 310, 231, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        
        
        self.Background_button_neutral_attack = QtWidgets.QLabel(self.centralwidget)
        self.Background_button_neutral_attack.setGeometry(QtCore.QRect(90, 310, 231, 101))
        self.Background_button_neutral_attack.setText("")
        self.Background_button_neutral_attack.setPixmap(QtGui.QPixmap("../sprites_ow/Bouton_rouge.png"))
        self.Background_button_neutral_attack.setObjectName("Background_button_neutral_attack") 
        
        self.Att_sp_bouton.setPalette(palette)
        self.Att_sp_bouton.setObjectName("Att_sp_bouton")
        self.fuite_bouton = QtWidgets.QPushButton(self.centralwidget)
        self.fuite_bouton.setGeometry(QtCore.QRect(90, 430, 231, 101))
        self.fuite_bouton.setObjectName("fuite_bouton")
        self.Chgt_pokemon_bouton = QtWidgets.QPushButton(self.centralwidget)
        self.Chgt_pokemon_bouton.setGeometry(QtCore.QRect(440, 430, 231, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.Chgt_pokemon_bouton.setPalette(palette)
        self.Chgt_pokemon_bouton.setObjectName("Chgt_pokemon_bouton")
        
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(20, -30, 771, 330))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("../sprites_ow/d843okx-eb13e8e4-0fa4-4fa9-968a-e0f36ff168de.png"))
        self.Background.setObjectName("Background") 
        
        self.Poekmon_Face = QtWidgets.QLabel(self.centralwidget)
        self.Poekmon_Face.setGeometry(QtCore.QRect(410, 110, 81, 81))
        self.Poekmon_Face.setText("")
        self.Poekmon_Face.setPixmap(QtGui.QPixmap("../Sprites_Pokemons/" + joueur.detecter(Pokemon_sauvage)[1].name.lower() + "_Face.png"))
        self.Poekmon_Face.setObjectName("Poekmon_Face")
        
        
        self.Pokemon_dos = QtWidgets.QLabel(self.centralwidget)
        self.Pokemon_dos.setGeometry(QtCore.QRect(160, 170, 81, 81))
        self.Pokemon_dos.setText("")
        self.Pokemon_dos.setPixmap(QtGui.QPixmap("../Sprites_Pokemons/" + joueur.pokemon_choisi.name.lower() + "_Dos.png"))
        self.Pokemon_dos.setObjectName("Pokemon_dos")
        
        self.Pokemon_Face_Nom = QtWidgets.QLabel(self.centralwidget)
        self.Pokemon_Face_Nom.setGeometry(QtCore.QRect(350, 80, 81, 31))
        self.Pokemon_Face_Nom.setObjectName("Pokemon_Face_Nom")
        
        self.Pokemon_Face_HP = QtWidgets.QLabel(self.centralwidget)
        self.Pokemon_Face_HP.setGeometry(QtCore.QRect(350, 130, 60, 13))
        self.Pokemon_Face_HP.setObjectName("Pokemon_Face_HP")
        
        self.Pokemon_Dos_HP = QtWidgets.QLabel(self.centralwidget)
        self.Pokemon_Dos_HP.setGeometry(QtCore.QRect(100, 190, 47, 13))
        self.Pokemon_Dos_HP.setObjectName("Pokemon_Dos_HP")
        
        self.Pokemon_Dos_Nom = QtWidgets.QLabel(self.centralwidget)
        self.Pokemon_Dos_Nom.setGeometry(QtCore.QRect(100, 140, 81, 31))
        self.Pokemon_Dos_Nom.setObjectName("Pokemon_Dos_Nom")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 340, 471, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../QtDesigner/depositphotos_537327850-stock-illustration-green-grass-meadow-small-white.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 340, 471, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../QtDesigner/depositphotos_537327850-stock-illustration-green-grass-meadow-small-white.jpg"))
        self.label_2.setObjectName("label_2")
        
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(-10, 60, 391, 291))
        # self.label_3.setText("")
        # self.label_3.setPixmap(QtGui.QPixmap("../QtDesigner/1863087_a0870.jpg"))
        # self.label_3.setObjectName("label_3")
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(-10, -20, 391, 291))
        # self.label_4.setText("")
        # self.label_4.setPixmap(QtGui.QPixmap("../QtDesigner/1863087_a0870.jpg"))
        # self.label_4.setObjectName("label_4")
        # self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(360, 0, 391, 291))
        # self.label_5.setText("")
        # self.label_5.setPixmap(QtGui.QPixmap("../QtDesigner/1863087_a0870.jpg"))
        # self.label_5.setObjectName("label_5")
        # self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(360, 60, 391, 291))
        # self.label_6.setText("")
        # self.label_6.setPixmap(QtGui.QPixmap("../QtDesigner/1863087_a0870.jpg"))
        # self.label_6.setObjectName("label_6")
        # self.label_7 = QtWidgets.QLabel(self.centralwidget)
        # self.label_7.setGeometry(QtCore.QRect(720, 70, 391, 291))
        # self.label_7.setText("")
        # self.label_7.setPixmap(QtGui.QPixmap("../QtDesigner/1863087_a0870.jpg"))
        # self.label_7.setObjectName("label_7")
        # self.label_8 = QtWidgets.QLabel(self.centralwidget)
        # self.label_8.setGeometry(QtCore.QRect(730, -10, 391, 291))
        # self.label_8.setText("")
        # self.label_8.setPixmap(QtGui.QPixmap("../QtDesigner/1863087_a0870.jpg"))
        # self.label_8.setObjectName("label_8")
        # self.label_8.raise_()
        # self.label_7.raise_()
        # self.label_6.raise_()
        # self.label_5.raise_()
        # self.label_3.raise_()
        # self.label_4.raise_()
        # self.label_2.raise_()
        # self.label.raise_()
        
        self.att_neutre_bouton.raise_()
        self.Att_sp_bouton.raise_()
        self.fuite_bouton.raise_()
        self.Chgt_pokemon_bouton.raise_()
        self.Poekmon_Face.raise_()
        self.Pokemon_dos.raise_()
        self.Pokemon_Face_Nom.raise_()
        self.Pokemon_Face_HP.raise_()
        self.Pokemon_Dos_HP.raise_()
        self.Pokemon_Dos_Nom.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 260, 750, 20))
        self.textBrowser.setObjectName("Barre_texte")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Combat Pokémon"))
        self.att_neutre_bouton.setText(_translate("MainWindow", "Attaque neutre"))
        self.Att_sp_bouton.setText(_translate("MainWindow", "Attaque spéciale"))
        self.fuite_bouton.setText(_translate("MainWindow", "Fuir"))
        self.Chgt_pokemon_bouton.setText(_translate("MainWindow", "Changer de Pokemon"))
        self.Pokemon_Face_Nom.setText(_translate("MainWindow", joueur.detecter(Pokemon_sauvage)[1].name))

        self.Pokemon_Face_HP.setText(_translate("MainWindow", "HP " + str(joueur.detecter(Pokemon_sauvage)[1].hp) + "/" + str(joueur.detecter(Pokemon_sauvage)[1].hp_init )))
        self.Pokemon_Dos_HP.setText(_translate("MainWindow", "HP " + str(joueur.pokemon_choisi.hp) + "/" + str(joueur.pokemon_choisi.hp_init)))
        self.Pokemon_Dos_Nom.setText(_translate("MainWindow", joueur.pokemon_choisi.name))

        # self.Pokemon_Face_HP.setText(_translate("MainWindow", "HP " + str(pokemon1.hp) + "/" + str(hp_init_pokemon1)))
        # self.Pokemon_Dos_HP.setText(_translate("MainWindow", "HP " + str(pokemon2.hp) + "/" + str(hp_init_pokemon2)))
        # self.Pokemon_Dos_Nom.setText(_translate("MainWindow", pokemon2.name))





# import Pokemon_face_rc


