from tkinter import messagebox
import PySimpleGUI as sg
import os
import pyautogui as pg
~ import subprocess

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
                                                                                                                                                                                                                                                                           