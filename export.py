from tkinter import messagebox
import PySimpleGUI as sg
import os
import pyautogui as pg
print("hello")
~ import subprocess
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Select a file to commit: "), sg.Input(key=""), sg.FileBrowse(key="-IN-")], [sg.Text(
    "Select a txt file: "), sg.Input(key=""), sg.FileBrowse(key="-INI-")], [sg.T("")],  [sg.Button("Commit"), sg.Button("Cancel")]]
~~~Building Window
window = sg.Window('Stedap Commits', layout, icon="sc.ico",
                   size=(600, 200), element_justification="center")


def push():
    path = values["-IN-"]
    folderpath = values["-INI-"]
    print(path)
    print(folderpath)
    if (path == "" and folderpath == ""):
        messagebox.showinfo(title="info", message="No directory selected")
    elif (folderpath == ""):
        messagebox.showinfo(
            title="info", message="Please select file path to commit from")
    elif (path == ""):
        messagebox.showinfo(
            title="info", message="Please select file to commit")
    else:
        ~ os.chdir(folderpath)
        ~ name = path.split("/")[-1]
        path2 = "/".join(path.split("/")[:-1])
        print(path2)
        ~ path3 = "/".join(folderpath.split("/")[:-1])
        os.chdir(path2)
        os.system("start cmd /K cd " + path2)
