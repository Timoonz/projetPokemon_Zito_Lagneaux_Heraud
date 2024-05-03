# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:56:57 2024

@author: Abigaëlle
"""

import pandas as pd
import POKEMON as p

types_pokemon = pd.read_csv('pokemon_first_gen.csv')
pokemons_map = pd.read_csv('pokemon_coordinates.csv')

Pokemon_map = []

for i in range (998) :
    for j in range (151) :
        
        if pokemons_map.iloc[i,0] == types_pokemon.iloc[j,1] :
            
            Pokemon_map.append(p.Pokemon(types_pokemon.iloc[j,1],types_pokemon.iloc[j,6], 
                                         types_pokemon.iloc[j,7],types_pokemon.iloc[j,8], 
                                         types_pokemon.iloc[j,9], types_pokemon.iloc[j,10], 
                                         types_pokemon.iloc[j,12],  pokemons_map.iloc[i,1]))
            