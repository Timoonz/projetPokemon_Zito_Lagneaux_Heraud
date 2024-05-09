# Importations

import pandas as pd
import POKEMON as p

types_pokemon = pd.read_csv('../data/pokemon_first_gen.csv')
pokemons_map = pd.read_csv('../data/pokemon_coordinates.csv')

Pokemon_sauvage = []

for i in range (998) :
    for j in range (151) :
        
        if pokemons_map.iloc[i,0] == types_pokemon.iloc[j,1] :
            
            if types_pokemon.iloc[j,2] == "Fire" :
            
                Pokemon_sauvage.append(p.Fire(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))
            
            if types_pokemon.iloc[j,2] == "Water" :
                
                Pokemon_sauvage.append(p.Water(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))
            
            if types_pokemon.iloc[j,2] == "Bug" :
                
                Pokemon_sauvage.append(p.Bug(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))
                
            if types_pokemon.iloc[j,2] == "Normal" :
                
                Pokemon_sauvage.append(p.Normal(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))
                
            if types_pokemon.iloc[j,2] == "Electric" :
                
                Pokemon_sauvage.append(p.Electric(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))
                
            if types_pokemon.iloc[j,2] == "Poison" :
                
                Pokemon_sauvage.append(p.Poison(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))               
                
            if types_pokemon.iloc[j,2] == "Ground" :
                
                Pokemon_sauvage.append(p.Ground(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))               
                
            if types_pokemon.iloc[j,2] == "Fairy" :
                
                Pokemon_sauvage.append(p.Fairy(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))              
                
            if types_pokemon.iloc[j,2] == "Fighting" :
                
                Pokemon_sauvage.append(p.Fighting(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))               
                
            if types_pokemon.iloc[j,2] == "Psychic" :
                
                Pokemon_sauvage.append(p.Psychic(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))              
                
            if types_pokemon.iloc[j,2] == "Ice" :
                
                Pokemon_sauvage.append(p.Ice(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))               
                
            if types_pokemon.iloc[j,2] == "Flying" :
                
                Pokemon_sauvage.append(p.Flying(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))              
                
            if types_pokemon.iloc[j,2] == "Dragon" :
                
                Pokemon_sauvage.append(p.Dragon(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))               
           
            if types_pokemon.iloc[j,2] == "Ghost" :
                
                Pokemon_sauvage.append(p.Ghost(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))           
            
            if types_pokemon.iloc[j,2] == "Rock" :
                
                Pokemon_sauvage.append(p.Rock(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))          
            
            if types_pokemon.iloc[j,2] == "Grass" :
                
                Pokemon_sauvage.append(p.Grass(types_pokemon.iloc[j,1],types_pokemon.iloc[j,5], 
                                             types_pokemon.iloc[j,6],types_pokemon.iloc[j,7], 
                                             types_pokemon.iloc[j,8], types_pokemon.iloc[j,9],
                                             types_pokemon.iloc[j,10],types_pokemon.iloc[j,12],  
                                             eval(pokemons_map.iloc[i,1])))            
                
                
                
                