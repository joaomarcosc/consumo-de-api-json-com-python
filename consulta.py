import requests
import json
import pandas
import csv

url = "http://data.fixer.io/api/latest?access_key=e81625589e4eeb69fb9a598fceae2552"

response = requests.get(url)

print(response.json())

if(response.status_code == 200):
  print("Done")
  print("Buscando informações")
  dados = response.json()


  euro = round(dados['rates']['BRL'] / dados['rates']['EUR'], 2)
  dollar = round(dados['rates']['BRL'] / dados['rates']['USD'], 2)
  real = 1
  bitcoin = round(dados['rates']['BRL'] / dados['rates']['BTC'], 2)
  
  print("Euro: ", euro)

  print("Dollar: ", dollar)

  print("Real: ", real)

  print("Bitcoin: ", bitcoin)


  tela = pandas.DataFrame({'Moedas':['Dolar', 'Euro', 'Real', 'Bitcoin'],'Valores':[dollar, euro, real, bitcoin]})
  tela.to_csv('valores.csv', index=False, sep=';', decimal=",")

else:
  print("Error")