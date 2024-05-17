# Importations
from abc import abstractmethod,ABCMeta
import numpy as np

from PyQt5.QtMultimedia import QSound


# Classes

### Classes Pokemon

class Pokemon (metaclass = ABCMeta):
    
    '''
    Cette classe abstraite est mère de tous les types de pokemons 
    et contient leurs attributs et comportements généraux
    '''
    
    def __init__(self, name ,hp ,atk, deff, sp_atk, sp_deff, legendary, speed,position):
        
        '''
        Création des attributs de chaque pokemon, indépendamment de leur type
        '''
        
        self.name = name
        self.hp = hp
        self.hp_init = hp
        self.atk = atk
        self.deff = deff
        self.sp_atk = sp_atk
        self.sp_deff = sp_deff
        self.speed = speed
        self.legendary = legendary
        
        #On définira comme position [-10,-10] pour les pokemons acquis pour les différencier des pokemons sauvages
        self.position = position 
        
        #Cette variable servira à afficher si le Pokémon est K.O. ou non lors du combat
        self.isKo = False                         
                                 

    def __str__(self) :
        
        
        '''
        Surcharge de la fonction str
        '''
        
        txt = str(self.name)
        
        return txt
    
        
    def attaque_neutre(self, ennemi):
        
        '''
        Cette méthode permet à un pokemon d'effectuer une attaque neutre
        '''

        degats = int(self.atk * 10 /ennemi.deff)
        
        return int(degats)
    
    
    @abstractmethod
    def attaque_speciale(self) :
        
        '''
        Cette fonction définit l'attaque spéciale d'un pokemon
        '''
        
        pass





class Fire (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,             
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 ,    
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    
    def type_pokemon(self) :
        
        return('Fire')    
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type feu
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



class Water (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type eau
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,           
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,    
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    
    def type_pokemon (self) :
        
        return 'Water'    
    
    
    def attaque_speciale (self, ennemi):

        '''
        Cette méthode définit l'attaque spéciale des pokemons de type eau
        '''        
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)


    
class Bug (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type insecte
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,              
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 1 ,  
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,    
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 0.5 , 
                           'Flying' : 0.5}
    
    
    def type_pokemon(self) :
        
        return('Bug')
    
    
    def attaque_speciale (self, ennemi):
 
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type insecte
        '''        
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



class Normal (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type normal
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 1}


    def type_pokemon(self) :
        
        return('Normal')        

        
    def attaque_speciale (self, ennemi):
 
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type insecte
        '''        
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)        
   
    
class Electric (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type electrik
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,              
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 ,    
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,    
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0 , 'Ghost' : 1 , 
                           'Flying' : 2}


    def type_pokemon(self) :
        
        return('Electric')
  
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type Electric
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



class Poison (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type poison
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                    
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 2 , 'Ice' : 1 ,          
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,        
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0.5 , 'Ghost' : 0.5 , 
                           'Flying' : 1}


    def type_pokemon(self) :
        
        return('Poison')
  
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type poison
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



class Ground (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type sol
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                
                           'Fire' : 2 , 'Electric' : 2 , 'Fairy' : 1 , 'Ice' : 0 ,      
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 2 ,  
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 0}


    def type_pokemon(self) :
        
        return('Ground')

    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type sol
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



class Fairy (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type fée
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 2 , 'Dragon' : 2 , 'Water' : 1 ,                
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,    
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 0.5 ,    
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Fairy')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type fée
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)


    
class Fighting (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type combat
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 2 ,    
                           'Bug' : 0.5 , 'Normal' : 2 , 'Grass' : 1 , 'Poison' : 0.5 ,  
                           'Psychic' : 0.5 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 0.5}


    def type_pokemon(self) :
        
        return('Fighting')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type combat
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



class Psychic (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type psy
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,                
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 2 ,      
                           'Psychic' : 0.5 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}


    def type_pokemon(self) :
        
        return('Psychic')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type psy
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



class Ice (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type glace
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 0.5 ,              
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 0.5 ,  
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 2}


    def type_pokemon(self) :
        
        return('Ice')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type glace
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)


    
class Flying (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type vol
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,                
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 ,    
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}


    def type_pokemon(self) :
        
        return('Flying')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type vol
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)


    
class Dragon (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type dragon
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 1 ,                
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0 , 'Ice' : 1 ,       
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}


    def type_pokemon(self) :
        
        return('Dragon')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type dragon
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)


    
class Ghost (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type spectre
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,       
                           'Bug' : 1 , 'Normal' : 0 , 'Grass' : 2 , 'Poison' : 1 ,      
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 2 , 
                           'Flying' : 1}


    def type_pokemon(self) :
        
        return('Ghost')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type spectre
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)


    
class Rock (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type roche
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,              
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 ,     
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 0.5 , 'Ghost' : 1 , 
                           'Flying' : 2}


    def type_pokemon(self) :
        
        return('Rock')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type roche
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)


    
class Grass (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type plante
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        #Ici on renseigne les forces et les faiblesses de ce type de pokémon envers les autres types 
        #En pratique, on enregistre les coefficients multiplicateurs sur les attaques sous la forme d'un dictionnaire
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,                  
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,        
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 0.5 ,    
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 0.5}


    def type_pokemon(self) :
        
        return('Grass')
    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spéciale des pokemons de type plante
        '''
        
        degats = (self.sp_atk * 10 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return int(degats)



### Classe Joueur
        
class Joueur :
    
    '''
    Cette classe contient les principales caractéristiques du joueur
    '''
    
    def __init__(self, name, position, rayon_de_vision = 0.25,pokemon_adverse = None, pokemon_choisi = Grass('Bulbasaur',45,49,49,65,65,45,False, [-10,-10]),
                 inventaire_de_pokemon = [Fire('Charmander',39,52,43,60,50,65,False, [-10,-10]),    # Nous avons choisi Salamèche, Bulbizarre et Carapuce
                                          Grass('Bulbasaur',45,49,49,65,65,45,False, [-10,-10]),    # comme pokemons de départ
                                          Water('Squirtle',44,48,65,50,64,43,False, [-10,-10])]) :
                                                                           
        self.name = name
        self.rdv = rayon_de_vision
        self.pokemon_choisi = pokemon_choisi
        self.position = position
        self.inventaire = inventaire_de_pokemon
    
    
    def chanter(self) :
        
        QSound.play("../sound/singing_player.wav")
        
        
    def choisir_un_pokemon (self) :
        
        # Inventaire = []
        
        # for i in self.inventaire :
        #     Inventaire.append(i.name)
        
        # print(Inventaire)
        
        # print("\nVeuillez-choisir votre pokemon")
        
        # pokemon_choisi = input()
        
        # i=0
        
        # while pokemon_choisi != self.inventaire[i].name :
        #     i+=1
            
        # return self.inventaire[i]
        
        pass
    
    def detecter(self, Pokemon_sauvage) :
        
        '''
        Cette fonction renvoit un Pokmeon si le joueur peut le voir
        '''
        
        
        # Création d'une liste contenant toutes les distances entre le joueur et les pokemons sauvages
        
        
        Distance = []
       
        for i in Pokemon_sauvage :
            
            d = np.sqrt((self.position[0]-i.position[0])**2 + (self.position[1]-i.position[1])**2 )
            
            if d not in Distance :
                
                Distance.append(d)
        
        
        
        # Vérifiation d'une possibilité de detection de pokémon
        for i in range(len(Distance)) :
            if Distance[i]<= self.rdv  :
                # print(Pokemon_sauvage[i].name)
                return True, Pokemon_sauvage[i]       # Si un pokemon est dans le champs de vision du joueur, ce pokemon est renvoyé
        
        return False, Pokemon_sauvage[0]
    
    
joueur = Joueur('joueur',[0,0])            

