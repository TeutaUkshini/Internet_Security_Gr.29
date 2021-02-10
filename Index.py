from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import urllib

def Scrape(arg=None):
    
    # Kontrollimi i url-se nese eshte e zbrazet
    if url_entry.get() == '':
        ms.showerror('Gabim', 'Shenoni nje URL valide !!!')
        
    else:
        try:
            ''' Fillon metoda Scraping '''
            # Dhenja e url-se
            url = url_entry.get()
            
            # Leximi i tere permbajtjes
            content = urllib.request.urlopen(url).read()
            
            # Kalimi i permbajtjes tek funksioni
            soup = BeautifulSoup(content, features="lxml")

            # Ruajtja e html ne nje variabel
            info = soup.prettify()
            '''Perfundimi i metodes Scrape '''

            '''Startimi i dritares(Window)'''
            # Krijimi i nje Dritareje(Window) te re
            root = tk.Toplevel()

            # Krijimi i titullit
            root.title('Falemnderit qe perdoret sherbimin tone !!!!')

            # Krijimi i ikones(logo)
            root.iconbitmap('img/logo.ico')

