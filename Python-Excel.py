import pandas as pd
import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.geeksforgeeks.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    pegando = link.get('href')
    if pegando not in urls:
        urls.append(pegando)   #Pegando URLS e alimenatando a lista


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
horas = []
for c in range(1,348):
    horas.append(current_time) #Igualando o length de horas com o de links = 347 ambos

dicionario = {}


dicionario['Links'] = urls
dicionario['Horas'] = horas



df = pd.DataFrame(data=dicionario)
df.to_excel("dicionario.xlsx", index=False) #Convertendo em Excel


#OBS: Eu não entendi a última parte do exercício

#OBS: Mas reafirmo que estou disposto EXTREMAMENTE disposto a aprender e contribuir gerando valor a empresa