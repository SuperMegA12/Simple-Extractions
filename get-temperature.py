def getTemperature (cep):
    import requests

    API_key = '15e582cd6693c8f08119cd35d98c9a8f' #Código da API de temperatura

    cep = input('Digite o CEP: ')
    if len(cep) != 8:
        print('CEP inválido')
        exit()

    r = requests.get(f'https://viacep.com.br/ws/{cep}/json/') #API do CEP

    dicionario = r.json()

    city_name = dicionario['localidade'] #Variável que pega o nome da cidade pelo json do CEP

    rua = dicionario['logradouro'] #VARIÁVEL que pega a Rua pelo json do CEP

    link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&lang=pt_br' #Link da API tempo

    request = requests.get(link)
    request_dic = request.json()
    description = request_dic['weather'][0]['description'] #Pegando a lista weather
    temperature = request_dic['main']['temp'] - 273.15 #Pegando a temperatura pela chave 'temp'
    print(f'A temperatura atual da cidade {city_name.upper()}, na Rua {rua}, é {temperature:.0f}ºC')


getTemperature('')
