##
## EPITECH PROJECT, 2022
## Untitled (Workspace)
## File description:
## sm_scrapper
##

from pywinauto.application import Application
import time
import sys
import glob
import os

actual_game = ""
actual_screen = None
main_screen = None
app = None

def start_game(game):
    global actual_game
    global main_screen
    global actual_screen
    global app
    actual_game = game[1]
    try:
        app = Application(backend="uia").start(actual_game)
    except:
        print("Error: game not found")
        return
    print("Waiting for game to start")
    time.sleep(2)
    try:
        main_screen = app.window(title=game[2])
        main_screen.wait('visible')
    except:
        try:
            main_screen = Application(backend="uia").connect(title=game[2])
            app = main_screen
            main_screen = main_screen.window(title=game[2])
            main_screen.wait('visible')
        except:
            print("Error: screen not found")
            return
    print("Main screen found")

def stop_game(game):
    app.kill()
    actual_game = ""
    actual_screen = None
    main_screen = None

def find_window(name):
    global actual_screen
    try:
        actual_screen = main_screen.window(title=name[1])
    except:
        print("Error: window not found")
        return


def print_game(game):
    print("Game: " + actual_game)

def print_screen(screen):
    print(actual_screen.print_control_identifiers())

def print_main_screen(screen):
    print(main_screen.print_control_identifiers())

def click(screen):
    try:
        actual_screen.set_focus()
        actual_screen.click_input()
    except:
        print("Error: button not found")
        return

def type_keys(screen):
    try:
        actual_screen.type_keys(screen[1])
    except:
        print("Error: text box not found")
        return

def help():
    print("start: start_game")
    print("stop: stop_game")
    print("connect: find_window")
    print("prg: print_game")
    print("prs: print_screen")

cmd_tab = {
    "start": start_game,
    "stop": stop_game,
    "connect": find_window,
    "prg": print_game,
    "prs": print_screen,
    "prm": print_main_screen,
    "help": help,
    "click": click,
    "type": type_keys
}

def sm_scrapper():
    while True:
        print("prompt $> ", end="")
        inp = input()
        parsed_inp = inp.split(" ")
        if parsed_inp[0] == "exit":
            break
        if parsed_inp[0] in cmd_tab:
            cmd_tab[parsed_inp[0]](parsed_inp)
