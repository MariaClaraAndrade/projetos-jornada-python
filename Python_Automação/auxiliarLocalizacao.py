import pyautogui
import time
import pandas

time.sleep(5)  # Give you 5 seconds to switch to the desired window

print (pyautogui.position())  # Get the current mouse position

tabela = pandas.read_csv("produtos.csv")
print (tabela)
