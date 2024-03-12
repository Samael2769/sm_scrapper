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
    time.sleep(2)
    app2 = Application(backend="uia").connect(title="Steam")
    app2.Steam.wait('visible')
    time.sleep(2)
    main_dlg = app2.window(title="Steam")
    main_dlg.set_focus()
    #print(main_dlg.print_control_identifiers())
    library_dlg = main_dlg.child_window(title="LIBRARY")
    library_dlg.set_focus()
    library_dlg.click_input()