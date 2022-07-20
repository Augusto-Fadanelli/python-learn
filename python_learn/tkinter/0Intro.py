# Aula <https://www.youtube.com/watch?v=AiBC01p58oI>
# Data: 19/04/2022

# sudo pacman -S tk
import tkinter

import pkg_resources
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

def cmdClick(texto:str):
    print(texto)

janela = Tk()
janela.title("Cotação de Moedas")
#janela.geometry('250x250') # Definir tamanho da janela
janela.resizable(width=False, height=False) # Impede de redimensionar

janela['bg'] = '#ffaa00' # Mudar cor de fundo

#janela.minsize(width=500, height=250) # Tamanho mínimo da janele
#janela.maxsize(width=700, height=500) # Tamanho máximo da janele
#janela.state("iconic") # Iniciar minimizado

# relief: solid, groove, flat, raised, sunken, ridge
texto_orientacao = Label(janela, text="Ver a cotação atual das moedas:", bg='yellow', fg='#ff10e0', font='Times 20 bold italic', width=40, bd=10, relief='raised')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Buscar cotações', command=pegarCotacoes, bg='#ffaa00')
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text="<vazio>", bg='#ffaa00')
texto_cotacoes.grid(column=0, row=2, pady=10)

cmdbutton1 = Button(janela, text='Executar', command=lambda: cmdClick('teste'), bg='#00ff00').grid(column=0, row=3)

Button(janela, text='Clicar', command=lambda: print('teste2'), bg='#ff0000').grid(column=0, row=4, pady=10)

# Deixar janela aberta
janela.mainloop()
