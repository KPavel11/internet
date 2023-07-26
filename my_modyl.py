from tkinter import *
from tkinter import ttk
import urllib.request
import webbrowser
import os
def examplecat():
    webbrowser.open_new_tab("http://examplecat.byethost8.com")
def my_github():
    webbrowser.open_new_tab('https://github.com/Evgenia89K')
def README():
    destination = 'README_Snake.md'
    url = 'https://raw.githubusercontent.com/Evgenia89K/snake/main/README.md'
    urllib.request.urlretrieve(url, destination)
    destination = 'Snake.pyw'
    url = 'https://raw.githubusercontent.com/Evgenia89K/snake/main/Snake/Snake.pyw'
    urllib.request.urlretrieve(url, destination)
    destination = 'Snake_E.pyw'
    url = 'https://raw.githubusercontent.com/Evgenia89K/snake/main/Snake/Snake_E.pyw'
    urllib.request.urlretrieve(url, destination)
    destination = 'Snake_R.pyw'
    url = 'https://raw.githubusercontent.com/Evgenia89K/snake/main/Snake/Snake_R.pyw'
    urllib.request.urlretrieve(url, destination)
    destination = 'functions_for_snake.py'
    url = 'https://raw.githubusercontent.com/Evgenia89K/snake/main/Snake/functions_for_snake.py'
    urllib.request.urlretrieve(url, destination)
def antiOpera():
    destination = 'README_Anti-Opera.md'
    url = 'https://raw.githubusercontent.com/Evgenia89K/Anti-Opera/main/README.md'
    urllib.request.urlretrieve(url, destination)
    destination = 'AntiOpera.py'
    url = 'https://raw.githubusercontent.com/Evgenia89K/Anti-Opera/main/AntiOpera.py'
    urllib.request.urlretrieve(url, destination)
    destination = 'anti-opera.py'
    url = 'https://raw.githubusercontent.com/Evgenia89K/Anti-Opera/main/anti-opera.py'
    urllib.request.urlretrieve(url, destination)
def Antivirus():
    destination = 'README_Antivirus.md'
    url = 'https://raw.githubusercontent.com/Evgenia89K/Antivirus/main/README.md'
    urllib.request.urlretrieve(url, destination)
    destination = 'Antivirus .py'
    url = 'https://raw.githubusercontent.com/Evgenia89K/Antivirus/main/Antivirus%20.py'
    urllib.request.urlretrieve(url, destination)
    destination = 'antivirus.py'
    url = 'https://raw.githubusercontent.com/Evgenia89K/Antivirus/main/antivirus.py'
    urllib.request.urlretrieve(url, destination)