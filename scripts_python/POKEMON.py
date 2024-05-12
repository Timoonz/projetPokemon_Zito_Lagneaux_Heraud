# Importations
from abc import abstractmethod,ABCMeta
import numpy as np


# Classes

### Classes Pokemon

class Pokemon (metaclass = ABCMeta):
    
    '''
    Cette classe abstraite est mère de tous les types de pokemons 
    et contient leurs attributs et comportements généraux
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        '''
        Création des attributs de chaque pokemon, independamment de leur type
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
        self.position = position # On définira comme position [-10,-10] pour les pokemons aquis
                                 # pour les différencier des pokemons sauvages

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

        degats = int(self.atk * 15 /ennemi.deff)
        
        return degats
    
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
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,            # Ici on reseigne les forces et  
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 ,    # les faiblesse du pokemon envers
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def type_pokemon(self) :
        
        return('Fire')    
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type feu
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



class Water (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type eau
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,            # Ici on reseigne les forces et
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def type_pokemon (self) :
        
        return 'Water'    
    
    def attaque_speciale (self, ennemi):

        '''
        Cette méthode définit l'attaque spécale des pokemons de type eau
        '''        
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats


    
class Bug (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type insecte
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,              # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 1 ,  # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,    # les autres types
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 0.5 , 
                           'Flying' : 0.5}
    
    def type_pokemon(self) :
        
        return('Bug')
    
    def attaque_speciale (self, ennemi):
 
        '''
        Cette méthode définit l'attaque spécale des pokemons de type insecte
        '''        
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



class Normal (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type normal
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Normal')        
        
    def attaque_speciale (self, ennemi):
 
        '''
        Cette méthode définit l'attaque spécale des pokemons de type insecte
        '''        
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats        
   
    
class Electric (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type electrik
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,              # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 ,    # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0 , 'Ghost' : 1 , 
                           'Flying' : 2}

    def type_pokemon(self) :
        
        return('Electric')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type Electric
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



class Poison (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type poison
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                    # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 2 , 'Ice' : 1 ,          # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,        # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0.5 , 'Ghost' : 0.5 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Poison')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type poison
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



class Ground (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type sol
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 2 , 'Electric' : 2 , 'Fairy' : 1 , 'Ice' : 0 ,      # les faiblesse du pokemon envers
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 2 ,  # les autres types
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 0}

    def type_pokemon(self) :
        
        return('Ground')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type sol
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



class Fairy (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type fée
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 2 , 'Dragon' : 2 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,    # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 0.5 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Fairy')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type fée
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats


    
class Fighting (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type combat
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 2 ,    # les faiblesse du pokemon envers
                           'Bug' : 0.5 , 'Normal' : 2 , 'Grass' : 1 , 'Poison' : 0.5 ,  # les autres types
                           'Psychic' : 0.5 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 0.5}

    def type_pokemon(self) :
        
        return('Fighting')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type combat
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



class Psychic (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type psy
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 2 ,      # les autres types
                           'Psychic' : 0.5 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Psychic')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type psy
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



class Ice (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type glace
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 0.5 ,              # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 0.5 ,  # les faiblesse du pokemon envers 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 2}

    def type_pokemon(self) :
        
        return('Ice')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type glace
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats


    
class Flying (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type vol
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 ,    # les faiblesse du pokemon envers
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Flying')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type vol
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats


    
class Dragon (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type dragon
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0 , 'Ice' : 1 ,      # les faiblesse du pokemon envers 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Dragon')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type dragon
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats


    
class Ghost (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type spectre
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers 
                           'Bug' : 1 , 'Normal' : 0 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 2 , 
                           'Flying' : 1}

    def type_pokemon(self) :
        
        return('Ghost')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type spectre
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats


    
class Rock (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type roche
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,              # Ici on reseigne les forces et
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 ,      # les faiblesse du pokemon envers 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 0.5 , 'Ghost' : 1 , 
                           'Flying' : 2}

    def type_pokemon(self) :
        
        return('Rock')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type roche
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats


    
class Grass (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type plante
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position)
        
        self.faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,                  # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,        # les faiblesse du pokemon envers
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 0.5 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 0.5}

    def type_pokemon(self) :
        
        return('Grass')
    
    def attaque_speciale (self, ennemi):
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type plante
        '''
        
        degats = (self.sp_atk * 15 / ennemi.sp_deff) * self.faiblesses[ennemi.type_pokemon()]
        
        return degats



### Classe Joueur
        
class Joueur :
    
    '''
    Cette classe contient les principale caractéristique du joueur
    '''
    
    def __init__(self, name, position, rayon_de_vision = 2, pokemon_choisi = Grass('Bulbasaur',45,49,49,65,65,45,False, [-10,-10]),
                 inventaire_de_pokemon = [Fire('Charmander',39,52,43,60,50,65,False, [-10,-10]),    # Nous avons choisi Salamèche, Bulbizarre et Carapuce
                                          Grass('Bulbasaur',45,49,49,65,65,45,False, [-10,-10]),    # comme pokemons de départ
                                          Water('Squirtle',44,48,65,50,64,43,False, [-10,-10])]) :
                                                                           
        self.name = name
        self.rdv = rayon_de_vision
        self.pokemon_choisi = pokemon_choisi
        self.position = position
        self.inventaire = inventaire_de_pokemon
        
    
    def se_deplacer (self) :
        
        pass
    
    
    def chanter(self) :
        
        print("Un jour je serais le meilleur dresseur")
        
        
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
        Cette fonction renvoit un Pokmeon sir le joueur peut le voir
        '''
        
        # Création d'une liste contenant toutes les distances entre le joueur et les pokemons sauvages
        Distance = []
        print ('lancement detection')
        for i in Pokemon_sauvage :
            
            d = np.sqrt((self.position[0]-i.position[0])**2 + (self.position[1]-i.position[1])**2 )
            
            Distance.append(d)
        
        # Vérifiation d'une possibilité de detection de pokémon
        for i in range(len(Distance)) :
            if Distance[i]<= self.rdv :
                print("Pokemon detecté")
                return True, Pokemon_sauvage[i]       # Si un pokemon est dans le champs de vision du joueur, ce pokemon est renvoyé
        
        return False, Pokemon_sauvage[635]
    
    
joueur = Joueur('joueur',[0,0])            

