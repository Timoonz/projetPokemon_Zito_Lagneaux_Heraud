# Importations
from abc import abstractmethod,ABCMeta


# Classes

### Classes Pokemon

class Pokemon (metaclass = ABCMeta):
    
    '''
    Cette classe abstraite est mère de tous les types de pokemons 
    et contient leurs attributs et comportements généraux
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        '''
        Création des attributs de chaque pokemon, independamment de leur type
        '''
        
        self.name = name
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.sp_atk = sp_atk
        self.sp_deff = sp_deff
        self.speed = speed
        self.legendary = legendary
        self.position = position # On définit comme position (-10,-10) pour les pokemons aquis
                                 # pour les différencier des pokemons sauvages

    def __str__(self) :
        
        
        '''
        Surcharge de la fonction str
        '''
        
        txt = str(self.name)
        
        return txt
    
        
    def attaque_neutre(self, enemi):
        
        '''
        Cette méthode permet à un pokemon d'effectuer une attaque neutre
        '''

        degats = int(self.atk * 15 /self.deff)
        
        return degats
    
    # @abstractmethod
    # def attaque_speciale(self) :
        
    #     '''
    #     Cette fonction définit l'attaque spéciale d'un pokemon
    #     '''
        
    #     pass





class Fire (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,            # Ici on reseigne les forces et  
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 ,    # les faiblesse du pokemon envers
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type feu
        '''
        
        pass



class Water (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type eau
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,            # Ici on reseigne les forces et
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():

        '''
        Cette méthode définit l'attaque spécale des pokemons de type eau
        '''        
        
        pass


    
class Bug (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type insecte
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,              # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 1 ,  # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,    # les autres types
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 0.5 , 
                           'Flying' : 0.5}
    
    def attaque_speciale ():
 
        '''
        Cette méthode définit l'attaque spécale des pokemons de type insecte
        '''        
        
        pass



class Normal (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type normal
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 1}
        
        
    def attaque_speciale ():
 
        '''
        Cette méthode définit l'attaque spécale des pokemons de type insecte
        '''        
        
        pass        
   
    
class Electric (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type electrik
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,              # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 ,    # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0 , 'Ghost' : 1 , 
                           'Flying' : 2}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type Electric
        '''
        
        pass



class Poison (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type poison
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                    # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 2 , 'Ice' : 1 ,          # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,        # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0.5 , 'Ghost' : 0.5 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type poison
        '''
        
        pass



class Ground (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type sol
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 2 , 'Electric' : 2 , 'Fairy' : 1 , 'Ice' : 0 ,      # les faiblesse du pokemon envers
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 2 ,  # les autres types
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 0}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type sol
        '''
        
        pass



class Fairy (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type fée
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 2 , 'Dragon' : 2 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,    # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 0.5 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type fée
        '''
        
        pass


    
class Fighting (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type combat
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 2 ,    # les faiblesse du pokemon envers
                           'Bug' : 0.5 , 'Normal' : 2 , 'Grass' : 1 , 'Poison' : 0.5 ,  # les autres types
                           'Psychic' : 0.5 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 0.5}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type combat
        '''
        
        pass



class Psychic (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type psy
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 2 ,      # les autres types
                           'Psychic' : 0.5 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type psy
        '''
        
        pass



class Ice (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type glace
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 0.5 ,              # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 0.5 ,  # les faiblesse du pokemon envers 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 2}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type glace
        '''
        
        pass


    
class Flying (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type vol
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 ,    # les faiblesse du pokemon envers
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type vol
        '''
        
        pass


    
class Dragon (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type dragon
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0 , 'Ice' : 1 ,      # les faiblesse du pokemon envers 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type dragon
        '''
        
        pass


    
class Ghost (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type spectre
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,                # Ici on reseigne les forces et
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,      # les faiblesse du pokemon envers 
                           'Bug' : 1 , 'Normal' : 0 , 'Grass' : 2 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 2 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type spectre
        '''
        
        pass


    
class Rock (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type roche
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,              # Ici on reseigne les forces et
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 ,      # les faiblesse du pokemon envers 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,      # les autres types
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 0.5 , 'Ghost' : 1 , 
                           'Flying' : 2}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type roche
        '''
        
        pass


    
class Grass (Pokemon) :
    
    '''
    Cette classe contient les pokemons de type plante
    '''
    
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10]):
        
        super().__init__(name,hp,atk,deff,sp_atk,sp_deff,legendary,speed,position = [-10,-10])
        
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,                  # Ici on reseigne les forces et
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 ,        # les faiblesse du pokemon envers
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 0.5 ,    # les autres types
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 0.5}
    
    def attaque_speciale ():
        
        '''
        Cette méthode définit l'attaque spécale des pokemons de type plante
        '''
        
        pass



### Classe Joueur
        
class Joueur :
    
    '''
    Cette classe contient les principale caractéristique du joueur
    '''
    
    def __init__(self, name, rayon_de_vision = 2, 
                 inventaire_de_pokemon = [Fire('Charmander',39,52,43,60,50,65,False, [-10,-10]),
                                          Grass('Bulbasaur',45,49,49,65,65,45,False, [-10,-10]),
                                          Water('Squirtle',44,48,65,50,64,43,False, [-10,-10])]) :
                                                                           
        self.name = name
        self.rdv = rayon_de_vision
        self.inventaire = inventaire_de_pokemon
        
    
    def se_deplacer (self) :
        
        pass
    
    
    def chanter(self) :
        
        print("Un jour je serais le meilleur dresseur")
        
        
    def choisir_un_pokemon (self) :
        
        Inventaire = []
        
        for i in self.inventaire :
            Inventaire.append(i.name)
        
        print(Inventaire)
        
        print("\nVeuillez-choisir votre pokemon")
        
        pokemon_choisi = input()
        
        i=0
        
        while pokemon_choisi != self.inventaire[i].name :
            i+=1
            
        return self.inventaire[i]
    
    
    def detecter(self, Pokemon_map) :
        
        return True 
            

