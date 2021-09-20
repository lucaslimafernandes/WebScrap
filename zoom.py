##Lucas Lima Fernandes

import time
#from datetime import datetime
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains 
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select
#from selenium.common.exceptions import NoSuchElementException
#import os
import pandas as pd
import csv
from timeit import default_timer as timer

print('program has started')
startTIME = timer()

url = 'https://www.zoom.com.br/search?q=monitor'

#Acesso browser
#browser = webdriver.Chrome() #Caso use Windows, deixar o webdriver na mesma pasta do script e usar esta variavel
browser = webdriver.Chrome('/usr/local/bin/chromedriver') #Caso use Linux -- instalar o webdriver sudo mv -f chromedriver /usr/local/bin/chromedriver
browser.get(url)
browser.maximize_window()

nomes = browser.find_elements_by_xpath("//span[@class='Cell_Name__jnsS-']")
preço = browser.find_elements_by_xpath("//strong[@class='Text_Text___RzD- Text_LabelMdBold__3KBIj CellPrice_MainValue__3s0iP']")

listNomes = [i.text for i in nomes]
listPreço = [i.text for i in preço]

for i in range(0, len(listNomes)):
    print(f'Produto: {listNomes[i]} - {listPreço[i]}')

