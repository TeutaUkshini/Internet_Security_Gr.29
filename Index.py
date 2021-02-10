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

# Bllokimi i zgjerimit te madhesise se dritares(Window)
            root.resizable(width=False, height=False)
            
            ''' Perfundimi i dritares(Window)'''
            
            # Shtimi i scrollbar ne dritare(window)
            scrollbar = Scrollbar(root)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Perdorimi i widget text per te shfaqur permbajtjen scraped
            text = Text(root, yscrollcommand=scrollbar.set, wrap = WORD)
            text.insert(INSERT, info)
            text.pack()

            # Scroll bar
            scrollbar.config(command=text.yview)

        except ValueError:
            ms.showerror('Gabim', 'Shenoni nje URL valide !!!')
    
'''Startimi i dritares(Window)'''
# Krijimi Widget
crawler = tk.Tk()

# Krijimi i madhesise se dritares(Window)
crawler.geometry('500x500')

# Bllokimi i madhesise se dritares(Window)
crawler.resizable(width=False, height=False)

# Krijimi i titullit
crawler.title('URL and structure crawling ')

# Krijimi i ikones(logo)
crawler.iconbitmap('img/logo.ico')
''' Perfundimi i dritares(Window) '''

# Korniza(Frame) Kryesore
top_frame = Label(crawler, text='WEB CRAWLER',font = ('Cosmic', 25, 'bold'), bg='cyan', fg='black', relief='groove',padx=500, pady=30, bd='5')
top_frame.pack(side='top')
