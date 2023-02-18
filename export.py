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
                