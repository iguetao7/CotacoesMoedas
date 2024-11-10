import requests
import json
import matplotlib.pyplot as plt


#API de cotações
cotacoes = requests.get("https://economia.awesomeapi.com.br/json/all")
cotacoes_dic = cotacoes.json()
print(cotacoes_dic)

#Preço atual do dólar, euro e bitcoin
print(f"Preço atual DÓLAR : R${cotacoes_dic['USD']['bid']}")
print(f"Preço atual EURO : R${cotacoes_dic['EUR']['bid']}")
print(f"Preço atual BITCOIN : R${cotacoes_dic['BTC']['bid']}")

#Cotações dólar e euro nos últimos 30 dias
cotacoes_dol30d = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/30")
cotacoes_dol_dic = cotacoes_dol30d.json()
lista_cotacoes_dol = [float(item["bid"]) for item in cotacoes_dol_dic]
lista_cotacoes_dol.reverse()
print(lista_cotacoes_dol)

cotacoes_eur30d = requests.get("https://economia.awesomeapi.com.br/json/daily/EUR-BRL/30")
cotacoes_eur_dic = cotacoes_eur30d.json()
lista_cotacoes_eur = [float(item["bid"]) for item in cotacoes_eur_dic]
lista_cotacoes_eur.reverse()
print(lista_cotacoes_eur)

#Gráficos dólar e euro 30 dias
plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_dol, label="Dólar")
plt.plot(lista_cotacoes_eur, label="Euro")
plt.legend()
plt.show()

#Cotação bitcoin nos últimos 360 dias
cotacoes_btc = requests.get("https://economia.awesomeapi.com.br/json/daily/BTC-BRL/365?start_date=20231109&end_date=20241109")
cotacoes_btc_dic = cotacoes_btc.json()
lista_cotacoes_btc = [float(item["bid"]) for item in cotacoes_btc_dic]
lista_cotacoes_btc.reverse()
print(lista_cotacoes_btc)

#Gráfico bitcoin 365 dias
plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_btc, label="Bitcoin")
plt.legend()
plt.show()
