import urllib.request
import json

from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://www.jw.org/pt/')
html = BeautifulSoup(page.read(), "html.parser")
metas = html.find_all('meta') #Variável com os valores das meta tags

array1 = []
for x in metas:
  array1.append(str(x).replace("<meta ", "").replace("/>", ""))

#Removendo strings desnecessárias para deixar só a chave e valor

arrayJson = []
for x in array1:
  arrayInterno = x.split("\" ")
  for y in arrayInterno:
    arrayInterno2 = y.split("=\"")
    x = {arrayInterno2[0].replace("\"", ""):arrayInterno2[1].replace("\"", "")} #Passando dados tratados para uma lista
    arrayJson.append(x)

jsonArray = json.dumps(arrayJson) #Transformando em formato JSON
print(jsonArray)


