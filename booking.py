##Lucas Lima Fernandes

import time
from datetime import datetime
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains 
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import os
import pandas as pd
import csv
from timeit import default_timer as timer

print('program has started')
startTIME = timer()

url = 'https://www.booking.com/index.pt-br.html'

#Acesso browser
#browser = webdriver.Chrome() #Caso use Windows, deixar o webdriver na mesma pasta do script e usar esta variavel
browser = webdriver.Chrome('/usr/local/bin/chromedriver') #Caso use Linux -- instalar o webdriver sudo mv -f chromedriver /usr/local/bin/chromedriver
browser.get(url)
browser.maximize_window()

time.sleep(2)
#btn_ = browser.find_element_by_xpath("//input[@value='Pesquisa']")
busca = browser.find_element_by_xpath("//input[@class='c-autocomplete__input sb-searchbox__input sb-destination__input']")
#busca = browser.find_element_by_xpath("//input[@value='Pesquisa']")
busca.send_keys('Gramado')

#clicando para abrir o calendário
data = browser.find_element_by_xpath("//span[@class='sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb']")
data.click()

data_in = '2021-08-02'
data_out = '2021-08-05'

#Preenchendo as datas
data = browser.find_element_by_xpath(f"//td[@data-date='{data_in}']")
data.click()
time.sleep(0.5)
data = browser.find_element_by_xpath(f"//td[@data-date='{data_out}']")
data.click()

#class='xp__guests__count'

btn_search = browser.find_element_by_xpath("//button[@class='sb-searchbox__button ']")
btn_search.click()

listHotelsNames = []
listHotelsRate = []
listHotelsPrice = []
listHotelsDistance = []

time.sleep(2)

for i in range(0, 4):

    hotelsNames = browser.find_elements_by_class_name('sr-hotel__name')
    hotelsRate = browser.find_elements_by_xpath("//div[@class='bui-review-score__badge']")
    #hotelsPrice = browser.find_elements_by_class_name('bui-price-display__value prco-inline-block-maker-helper ')
    hotelsPrice = browser.find_elements_by_xpath("//div[@class='bui-price-display__value prco-inline-block-maker-helper ']")
    hotelsDistance = browser.find_elements_by_class_name('sr_card_address_line__user_destination_address')

    #print(hotelsPrice)
    #hotels = {}
    cont = 0

    #print(hotelsRate)

    for i in hotelsNames:
        #print(f'entrou for: {cont}')
        #print(f'hotelName: {i.text}')
        #print(f'hotelsRate: {hotelsRate[cont].text}')
        #print(f'hotelPrice: {hotelsPrice[cont].text}')
        listHotelsNames.append(i.text)
        #print(f'{i.text} cont: {cont}')
        listHotelsRate.append(hotelsRate[cont].text)
        listHotelsPrice.append(hotelsPrice[cont].text)
        listHotelsDistance.append(hotelsDistance[cont].text)
        
        #hotels[i.text] = hotelsRate[cont].text
        cont+=1

    print(i)
    btn_nextPage = browser.find_element_by_xpath("//a[@title='Página seguinte']")
    btn_nextPage.click()
    time.sleep(5)

#pegar os dados da última página clicada
#listHotelsNames.append(i.text)
#listHotelsRate.append(hotelsRate[cont].text)
#listHotelsPrice.append(hotelsPrice[cont].text)

hotels = {
    'hotelNames': listHotelsNames,
    'hotelPrice': listHotelsPrice,
    'hotelRate': listHotelsRate,
    'centreDistance': listHotelsDistance
    }

#print(hotels)


#Salvando em Pandas DataFrame
save_df = pd.DataFrame(hotels)

save_df.to_excel('export/Extracao_BOOKING.xlsx')

endTIME = timer()
print('Terminou a extração!')
print(f'seconds: {startTIME - endTIME}')
print(f'minutes: {(startTIME - endTIME)/60}')
#Fim