~ import subprocess
import pyautogui as pg
import os
import PySimpleGUI as sg
from tkinter import messagebox


sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Select a file to commit: "), sg.Input(key="") , sg.FileBrowse(key="-IN-")], [sg.Text("Select a txt file: "), sg.Input(key="") , sg.FileBrowse(key="-INI-")], [sg.T("")],  [sg.Button("Commit"), sg.Button("Cancel")]]
~~~Building Window
