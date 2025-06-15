import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

#Entar no site:

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click (x=943, y=599)
time.sleep(3)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#Fazer login:

time.sleep(3)
pyautogui.click (x=699, y=511)
pyautogui.write('meuemailficticio@gmail.com')
pyautogui.press('tab')
pyautogui.write('senhaficticia123')   
pyautogui.press('enter')


time.sleep(3)

#importar a planilha com os produtos
tabela = pandas.read_csv("produtos.csv")

print (tabela)

#Cadastrar o primeiro produto
for linha in tabela.index:
    pyautogui.click (x=896, y=373)

    codigo = tabela.loc[linha, 'codigo']    
    pyautogui.write(codigo)

    pyautogui.press('tab')
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab')
    categoria = str (tabela.loc[linha, 'categoria']) ## Converte o dado numérico para string
    pyautogui.write(categoria)  

    pyautogui.press('tab')
    preco_unitario = str (tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario) 

    pyautogui.press('tab') 
    custo = str (tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab')
    obs = str (tabela.loc[linha, 'obs']) # Nesse caso, converte um NaN para string

    if obs != 'nan':
        pyautogui.write(obs)
    else:
        pyautogui.write('')

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll (10000) #sobe a tela para o topo
    