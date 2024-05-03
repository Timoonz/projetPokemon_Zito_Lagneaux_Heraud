from abc import abstractmethod,ABCMeta

class Pokemon (metaclass = abc.ABCmeta):
    
    '''
    Cette classe abstraite est mère de tous les types de pokemons 
    et contient leurs attributs et comportements généraux
    '''
    def __init__(self,name,hp,atk,deff,sp_atk,sp_deff,speed,position = (-10,-10)):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.sp_atk = sp_atk
        self.sp_deff = sp_deff
        self.speed = speed
        self.position = position


    def attaque_neutre():
        '''
        Cette méthode permet à un pokemon d'effectuer une attaque neutre
        '''
        

        pass







class Fire:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 , 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass

class Water:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 0.5 ,
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass
    
    
class Bug:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 0.5 , 
                           'Flying' : 0.5}
    
    def attaque_speciale ():
        
        
        pass
    
class Normal:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 1}
    
   
    
class Electric:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0 , 'Ghost' : 1 , 
                           'Flying' : 2}
    
    def attaque_speciale ():
        
        
        pass
    
class Poison:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 2 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 0.5 ,
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 0.5 , 'Ghost' : 0.5 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass
    
class Ground:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 2 , 'Electric' : 2 , 'Fairy' : 1 , 'Ice' : 0 , 
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 2 ,
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 0}
    
    def attaque_speciale ():
        
        
        pass
    
class Fairy:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 2 , 'Dragon' : 2 , 'Water' : 1 ,
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 0.5 ,
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass
    
class Fighting:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0.5 , 'Ice' : 2 , 
                           'Bug' : 0.5 , 'Normal' : 2 , 'Grass' : 1 , 'Poison' : 0.5 ,
                           'Psychic' : 0.5 , 'Rock' : 2 , 'Ground' : 1 , 'Ghost' : 0 , 
                           'Flying' : 0.5}
    
    def attaque_speciale ():
        
        
        pass
    
class Psychic:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 2 ,
                           'Psychic' : 0.5 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass
    
class Ice:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 0.5 ,
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 0.5 , 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 2}
    
    def attaque_speciale ():
        
        
        pass
    
class Flying:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 2 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 1 , 'Electric' : 0.5 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 2 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 0.5 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass
    
class Dragon:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 2 , 'Water' : 1 ,
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 0 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 1 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass
    
class Ghost:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 1 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 1 , 'Normal' : 0 , 'Grass' : 2 , 'Poison' : 1 ,
                           'Psychic' : 2 , 'Rock' : 1 , 'Ground' : 1 , 'Ghost' : 2 , 
                           'Flying' : 1}
    
    def attaque_speciale ():
        
        
        pass
    
class Rock:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 0.5 , 'Dragon' : 1 , 'Water' : 1 ,
                           'Fire' : 2 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 2 , 
                           'Bug' : 2 , 'Normal' : 1 , 'Grass' : 1 , 'Poison' : 1 ,
                           'Psychic' : 1 , 'Rock' : 1 , 'Ground' : 0.5 , 'Ghost' : 1 , 
                           'Flying' : 2}
    
    def attaque_speciale ():
        
        
        pass
    
class Grass:
    '''
    Cette classe contient les pokemons de type feu
    '''
    
    def __init__(self):
        self.Faiblesses = {'Fighting' : 1 , 'Dragon' : 0.5 , 'Water' : 2 ,
                           'Fire' : 0.5 , 'Electric' : 1 , 'Fairy' : 1 , 'Ice' : 1 , 
                           'Bug' : 0.5 , 'Normal' : 1 , 'Grass' : 0.5 , 'Poison' : 0.5 ,
                           'Psychic' : 1 , 'Rock' : 2 , 'Ground' : 2 , 'Ghost' : 1 , 
                           'Flying' : 0.5}
    
    def attaque_speciale ():
        
        
        pass