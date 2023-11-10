import pyautogui
import webbrowser
from time import sleep

numero = "+524448434351"
texto = "Te estoy escribiendo desde un bot que hice en mi computadora"
rango = 1
webbrowser.open("https://wa.me/" + numero)
sleep(10)
for i in range(rango):
    pyautogui.typewrite(texto)
    pyautogui.press("enter")
    print("Mensaje enviado")
