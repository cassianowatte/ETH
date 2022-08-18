from cProfile import label
from ctypes.wintypes import SIZE
from multiprocessing.sharedctypes import Value
from tkinter import font
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *


def ethereum():
    options = webdriver.ChromeOptions()  # condição para deixar invisivel o navegador
    options.add_argument('--headless')
    navegador = webdriver.Chrome(options=options)  # abre google crhome
    navegador.get('https://www.google.com.br/')  # entrar no google
    navegador.find_element(
        'xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação ethereum')  # campo de busca
    navegador.find_element(
        'xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    time.sleep(5)  # tempo de espera para carregar
    # pega o valor atual da moeda
    eth = navegador.find_element(
        'xpath', '//*[@id="crypto-updatable_2"]/div[3]/div[5]/div[2]/input').get_attribute('value')

    texto = (f'Valor do Ethereum: {eth} Reais atualizado')
    texto_cotacao['text'] = texto


# interface grafica
janela = Tk()
janela.geometry('400x200')
janela.title('Cotação Ethereum')

texto_orientação = Label(janela, text='Cotação Atual Ethereum', font='Arial')
texto_orientação.pack()
botao = Button(janela, text='Clicar', height=3, width=20, command=ethereum)
botao.pack()
texto_cotacao = Label(janela, text='', font='Arial')
texto_cotacao.pack()
janela = mainloop()
