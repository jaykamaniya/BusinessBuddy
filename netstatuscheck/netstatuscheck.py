import os
import sys
import socket
import urllib.request

from tkinter import *

mainwindow = Tk()
mainwindow.geometry('700x400')
mainwindow.title('BizzHub')


def online():
    global welcomepg
    welcomepg=Label(mainwindow,text="Welcome to online BizzHub")
    welcomepg.grid(column=30,row=10)

def offline():
    print('rtyhuj')
    
def connect(host='http://google.com'):
    global netstatus
    try:
        urllib.request.urlopen(host)
        netstatus="Online"
        online()
        return True
    except:
        netstatus="Offline"
        offline()
        return False
print( 'connected' if connect() else 'no internet!' )

netlbl= Label(mainwindow,text=netstatus)
netlbl.grid(column=0, row=10)

mainwindow.mainloop()

