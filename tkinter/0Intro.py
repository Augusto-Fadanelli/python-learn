# Aula <https://www.youtube.com/watch?v=AiBC01p58oI>
# Data: 19/04/2022

# sudo pacman -S tk

import requests
from tkinter import *

def pegarCotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'Dólar: {cotacao_dolar}\nEuro: {cotacao_euro}\nBTC: {cotacao_btc}'

    texto_cotacoes["text"] = texto

janela = Tk()
janela.title("Cotação de Moedas")
#janela.geometry('250x250') # Definir tamanho da janela

texto_orientacao = Label(janela, text="Ver a cotação atual das moedas:")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Buscar cotações', command=pegarCotacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text="<vazio>")
texto_cotacoes.grid(column=0, row=2, pady=10)

# Deixar janela aberta
janela.mainloop()
