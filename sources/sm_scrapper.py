##
## EPITECH PROJECT, 2022
## Untitled (Workspace)
## File description:
## sm_scrapper
##

from pywinauto.application import Application
import time

def sm_scrapper():
    app = Application(backend="uia").start(r"D:\Games\Steam\steam.exe")
    app2 = Application(backend="uia").connect(title="Steam")
    app2.Steam.wait('visible')
    time.sleep(5)
    print(app2.windows())
    #main_dlg = app.window(title="Steam")
    #main_dlg.wait('visible')