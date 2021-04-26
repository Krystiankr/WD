#Zadanie 1
from typing import List
import pandas as pd

info=['color','director_name','num_critic_for_reviews','duration','director_facebook_likes','actor_3_facebook_likes','actor_2_name','actor_1_facebook_likes','gross','genres','actor_1_name','movie_title','num_voted_users','cast_total_facebook_likes','actor_3_name','facenumber_in_poster','plot_keywords','movie_imdb_link','num_user_for_reviews','language','country','content_rating','budget','title_year','actor_2_facebook_likes','imdb_score','aspect_ratio','movie_facebook_likes']

movie_new: pd.DataFrame = pd.read_csv('movie_new.csv', sep=';', names=info, header=None)

#Zadanie 2

movie_num: pd.DataFrame = movie_new.select_dtypes('number')

#Zadanie 3

from typing import Dict

mapping: Dict[str, float] = {}

for kol in movie_num.columns:
    if movie_num[kol].isnull().any():      
        mapping[kol] =movie_num[kol].mean() 

movie_num.fillna(mapping) 

#Zadanie 4

movie_num.describe().loc['std'].idxmax()

#Zadanie 5

movie_new.fillna(movie_num)

#Zadanie 6

for kol in movie_new.columns:
    movie_new = movie_new.fillna({kol:movie_new.at[0, kol]})

#Zadanie 7

for el in range(0, len(movie_new)):
    e1: str = str(movie_new.at[el, 'director_name'])
    e2: str = str(movie_new.at[el, 'movie_title'])
    movie_new = movie_new.rename(index = {el : (e1+" - " + e2)})

#Zadanie 8

for el in movie_new.index:
    movie_new.at[el,'imdb_score'] += 1

#Zadanie 9

for tytul in movie_new.columns:
    nazwa: str = tytul.title().replace('_','')
    movie_new = movie_new.rename(columns = {tytul:nazwa})

#Zadanie 10

import random
a: int = randint(0, 4)
b: int = randint(5, 10)

movie_random: pd.DataFrame = movie_new.iloc[a:b]

#Zadanie 11

from pandas.api.types import is_string_dtype

from typing import List
lista: List[int] = []

for row in movie_random.index:
    lista.append(row)

for kol in movie_random.columns:
    if not(is_string_dtype(movie_random[kol])):
        value: int = randint(30, 50)
        choicee: str = random.choice(lista)
        movie_random.at[choicee, kol] += 1
		
		
		
		
		
		
