from tkinter import messagebox
import PySimpleGUI as sg
import os
import pyautogui as pg
~ import subprocess
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Select a file to commit: "), sg.Input(key=""), sg.FileBrowse(key="-IN-")], [sg.Text(
    "Select a txt file: "), sg.Input(key=""), sg.FileBrowse(key="-INI-")], [sg.T("")],  [sg.Button("Commit"), sg.Button("Cancel")]]
~~~Building Window
~ pg.click()
~ pg.sleep(1)
~ pg.write(i)
~ pg.hotkey("ctrl", "s")
~ pg.click(1127, 1054)
~ pg.write("git add .")
~ pg.press("enter")
~ pg.sleep(3)
~ pg.write("git commit -m 'Update'")
~ pg.press("enter")
~ pg.sleep(3)
~ pg.write("git push origin main")
~ pg.press("enter")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Commit":
                    push()
                elif event == "Cancel":
                        