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
#import csv
from timeit import default_timer as timer


print('program has started')
startTIME = timer()


## Listas para salvar os dados
uf = []
municipio = []
renasem = []
validade = []
atividade = []
cpf_cnpj = []
nome = []
endereco = []
cep = []

#URL de acesso
url = 'https://sistemasweb.agricultura.gov.br/renasem/psq_consultarenasems.do'

#Acesso browser
#browser = webdriver.Chrome() #Caso use Windows, deixar o webdriver na mesma pasta do script e usar esta variavel
browser = webdriver.Chrome('/usr/local/bin/chromedriver') #Caso use Linux -- instalar o webdriver sudo mv -f chromedriver /usr/local/bin/chromedriver

browser.get(url)
browser.maximize_window()

#browser pesquisa
btn_ = browser.find_element_by_xpath("//input[@value='Pesquisa']")
btn_.click()

#Tempo de espera para carregar a página
time.sleep(2)

#Função para raspagem dos dados
def getData():

    #Busca da table pela class
    tabl_ = browser.find_elements_by_xpath(".//table[@class='labelCampo']")[1]
    df = pd.read_html(tabl_.get_attribute('innerHTML'))
    

    #Excluindo linhas em branco -- sugestão futura, executar em bloco try/except, para excluir linha 14
    df = df[0].drop([0,1,2,3], axis=0)
    #Excluindo colunas em branco
    df.drop([9, 10], axis=1, inplace=True)

    columns_ = {0:'UF',1:'Municipio',2:'RENASEM',3:'Validade',4:'Atividade',5:'CPF_CNPJ',6:'Nome',7:'Endereco',8:'CEP'}
    df.rename(columns=columns_, inplace=True)
    dict_ = df.to_dict('list')

    #laço for para salvar os dados nas lista auxiliares    
    for i in range(0, len(dict_['UF'])):
        uf.append(dict_['UF'][i])
        municipio.append(dict_['Municipio'][i])
        renasem.append(dict_['RENASEM'][i])
        validade.append(dict_['Validade'][i])
        atividade.append(dict_['Atividade'][i])
        cpf_cnpj.append(dict_['CPF_CNPJ'][i])
        nome.append(dict_['Nome'][i])
        endereco.append(dict_['Endereco'][i])
        cep.append(dict_['CEP'][i])
        
#Executar a função de raspagem na primeira página
getData()

cont = 0
#Para exemplo, executando o for para as primeiras páginas
#Caso queira ir até o final, executar o laço while
#for c in range(0, 4000):
#while True:
for c in range(0, 9):
    cont += 1
    print(f'Page: {cont}')
    btn_Next = browser.find_element_by_xpath("//img[@title='Próximo']")
    
    if btn_Next.get_attribute('onclick') in ['', ' ', None, False]:
        print('End of pages!')
        break
    
    else:
        btn_Next.click()
        getData()

#Salvando em Pandas DataFrame
save_df = pd.DataFrame({
            'UF': uf, 
            'Municipio': municipio, 
            'RENASEM': renasem, 
            'Validade': validade, 
            'Atividade': atividade,
            'CPF_CNPJ': cpf_cnpj,
            'Nome': nome,
            'Endereco': endereco,
            'CEP':cep
            })

save_df.to_excel('export/Extração_SIGEF_RENASEMS.xlsx')

endTIME = timer()
print('Terminou a extração!')
print(f'seconds: {startTIME - endTIME}')
print(f'minutes: {(startTIME - endTIME)/60}')
#Fim