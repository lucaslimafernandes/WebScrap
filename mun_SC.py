"""
Script para conhecimento da biblioteca Beatiful Soup
Tutorial de Odemir Depieri Jr
https://www.linkedin.com/posts/odemir-depieri-jr_guia-sobre-o-beautiful-soup-activity-6803804448339574784-hfe-/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Santa_Catarina'

page = requests.get(url)
colect = bs(page.text, 'html.parser')

#document html
#print()

#Title of page
#print(colect.title)

#Only title string
#print(colect.title.string)

#Tag name
#print(colect.title.name)

#Finding class by class name
#finding = colect.find(class_='p-search--show-thumbnail')
#print(finding)

#Returns all tags
#print(colect.p)
#print(colect.div)
#print(colect.a)

#Identificar class name de uma tag
#print(colect.a['class'])
#print(colect.span['class'])

#Todas as tags com um parametro
#print(colect.find_all('a'))


#Procurar por um id
#print(colect.find(id='p-search'))


#Percorrer em loop para coleter os links
#for link in colect.find_all('a'):
#    print(f'Links: {link.get("href")}')


#Coleta somente de textos
#print(colect.get_text())

### COLETA DOS DADOS DA TABELA DE MUNICIPIOS

#Coleta tbody em uma lista
tables = list(colect.find_all('tbody'))
#print(tables)

#Listas auxiliares
cities = []
state = []
Id = []

c = 0

for text in tables[1].find_all():

    city = text.string

    if city == None:
        pass

    else:
        cities.append(city)
        state.append('Santa Catarina')
        Id.append(c)

        c+=1

data = {
    'Id':Id,
    'City':cities,
    'State':state
}

df = pd.DataFrame(data)

df.to_csv('export/Santa_Catarina.csv')

"""Saída dos dados apresentou alguns erros,
porém o script foi realizado conforme o guia/tutorial
para aprendizado da biblioteca."""
