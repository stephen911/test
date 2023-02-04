import os
import PySimpleGUI as sg
from tkinter import messagebox
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Select a file to commit: "), sg.Input(key=""), sg.FileBrowse(key="-IN-")], [sg.Text(
    "Select a txt file: "), sg.Input(key=""), sg.FileBrowse(key="-INI-")], [sg.T("")],  [sg.Button("Commit"), sg.Button("Cancel")]]
~~~Building Windowwindow = sg.Window('Stedap Commits', layout, icon="sc.ico", size=(600, 200), element_justification="center")


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
        
        