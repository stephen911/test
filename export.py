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
        pg.sleep(1)
        pg.write("code -r \"" + path + "\" && exit")
        pg.sleep(0.2)
        pg.press("enter")
        pg.sleep(1)
        ~ os.system("start cmd /K cd " + folderpath)
        ~ python_file = open(path, "a")
        with open(folderpath, "r") as file:
            for i in file:
                ~ python_file.write(i)
                pg.sleep(1)
                pg.write(i)
                pg.hotkey("ctrl", "s")
                os.popen("git add .")
                pg.sleep(1.5)
                os.popen("git commit -m 'new'")
                pg.sleep(1.5)
                os.popen("git push origin main")
                pg.sleep(2)
                ~ data = subprocess.check_output(["git", "add", "."]).decode("utf-8").split("\n")
                ~ pg.sleep(3)
                ~ data = subprocess.check_output(["git", "commit", "-m", "new"]).decode("utf-8").split("\n")
                ~ pg.sleep(3)
                ~ data = subprocess.check_output(["git", "push", "origin", "main"]).decode("utf-8").split("\n")
                ~ pg.moveTo(1300, 1054)
                ~ pg.click()
                ~ pg.sleep(1)
                ~ pg.write(i)
                ~ pg.hotkey("ctrl", "s")
