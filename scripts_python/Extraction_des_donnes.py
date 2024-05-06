# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:56:57 2024

@author: Abigaëlle
"""

import pandas as pd
import POKEMON as p

types_pokemon = pd.read_csv('../data/pokemon_first_gen.csv')
pokemons_map = pd.read_csv('../data/pokemon_coordinates.csv')

Pokemon_map = []

for i in range (998) :
    for j in range (151) :
        
        if pokemons_map.iloc[i,0] == types_pokemon.iloc[j,1] :
            
            if types_pokemon.iloc[j,2] == "Fire" :
            
                Pokemon_map.append(p.Fire(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                             types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                             types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                             types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                             pokemons_map.iloc[i,1]))
            
            if types_pokemon.iloc[j,2] == "Water" :
                
                Pokemon_map.append(p.Water(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                           types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                           types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                           types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                           pokemons_map.iloc[i,1]))
            
            if types_pokemon.iloc[j,2] == "Bug" :
                
                Pokemon_map.append(p.Bug(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                         types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                         types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                         types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                         pokemons_map.iloc[i,1]))
                
            if types_pokemon.iloc[j,2] == "Normal" :
                
                Pokemon_map.append(p.Normal(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                            types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                            types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                            types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                            pokemons_map.iloc[i,1]))
                
            if types_pokemon.iloc[j,2] == "Electric" :
                
                Pokemon_map.append(p.Electric(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                              types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                              types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                              types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                              pokemons_map.iloc[i,1]))
                
            if types_pokemon.iloc[j,2] == "Poison" :
                
                Pokemon_map.append(p.Poison(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                            types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                            types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                            types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                            pokemons_map.iloc[i,1]))                
                
            if types_pokemon.iloc[j,2] == "Ground" :
                
                Pokemon_map.append(p.Ground(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                            types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                            types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                            types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                            pokemons_map.iloc[i,1]))                
                
            if types_pokemon.iloc[j,2] == "Fairy" :
                
                Pokemon_map.append(p.Fairy(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                           types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                           types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                           types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                           pokemons_map.iloc[i,1]))                
                
            if types_pokemon.iloc[j,2] == "Fighting" :
                
                Pokemon_map.append(p.Fighting(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                              types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                              types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                              types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                              pokemons_map.iloc[i,1]))                
                
            if types_pokemon.iloc[j,2] == "Psychic" :
                
                Pokemon_map.append(p.Psychic(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                             types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                             types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                             types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                             pokemons_map.iloc[i,1]))                
                
            if types_pokemon.iloc[j,2] == "Ice" :
                
                Pokemon_map.append(p.Ice(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                         types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                         types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                         types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                         pokemons_map.iloc[i,1]))                
                
            if types_pokemon.iloc[j,2] == "Flying" :
                
                Pokemon_map.append(p.Flying(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                            types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                            types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                            types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                            pokemons_map.iloc[i,1]))                
                
            if types_pokemon.iloc[j,2] == "Dragon" :
                
                Pokemon_map.append(p.Dragon(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                            types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                            types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                            types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                            pokemons_map.iloc[i,1]))                
           
            if types_pokemon.iloc[j,2] == "Ghost" :
                
                Pokemon_map.append(p.Ghost(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                           types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                           types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                           types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                           pokemons_map.iloc[i,1]))            
            
            if types_pokemon.iloc[j,2] == "Rock" :
                
                Pokemon_map.append(p.Rock(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                          types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                          types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                          types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                          pokemons_map.iloc[i,1]))            
            
            if types_pokemon.iloc[j,2] == "Grass" :
                
                Pokemon_map.append(p.Grass(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                           types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                           types_pokemon.iloc[j,9], types_pokemon.iloc[j,10],
                                           types_pokemon.iloc[j,11],types_pokemon.iloc[j,12],  
                                           pokemons_map.iloc[i,1]))            
                
                
                
                