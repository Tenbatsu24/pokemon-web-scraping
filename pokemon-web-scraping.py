#!/usr/bin/env python
# coding: utf-8

# In[1]:


from lxml import html
import requests

import pandas as pd
import numpy as np

# ###### Get the page which we will scrape

# In[2]:


url = 'https://pokemondb.net/pokedex/national'
page = requests.get(url)

# ###### Use the library function to create xml tree

# In[3]:


tree = html.fromstring(page.content)

# ###### Find the Pokedex entry for the pokemon

# In[4]:


pokedex_numbers = np.array(tree.xpath('//div//small/text()'), dtype=np.str)
pokedex_numbers = [entry for entry in pokedex_numbers if entry[0] == '#']

## pokedex = pd.DataFrame(data=pokedex_numbers, columns=["pokedex_number"])


# ###### Get some of the details of the pokemon

# In[5]:


pokemon_names = np.array(tree.xpath('//a[@class = "ent-name"]/text()'), dtype=np.str)
pokemon_name_type = np.array(tree.xpath('//div[@class ="infocard "]//a/text()'), dtype=np.str)
pokemon_type = {}
current_key = None
for entry in pokemon_name_type:
    print(pokemon_type)
    if entry in pokemon_names:
        current_key = entry
    else:
        if current_key not in pokemon_type.keys():
            pokemon_type[current_key] = []
        pokemon_type[current_key].append(entry)
print(pokemon_type)