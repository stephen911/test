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
                                                
                                                        exit(0)
                                                                ~ print(values["-IN-"])
                                                                
                                                                
                                                                
                                                                
                                                                        ~ data = subprocess.check_output(["git", "add", "."]).decode("utf-8").split("\n")
                                                                                ~ pg.sleep(3)
                                                                                        ~ data = subprocess.check_output(["git", "commit", "-m", "new"]).decode("utf-8").split("\n")
                                                                                                ~ pg.sleep(3)
                                                                                                        ~ ~ data = subprocess.check_output(["git", "config", "--global", "rebase.autoStash", "true"]).decode("utf-8").split("\n")
                                                                                                                ~ pg.sleep(3)
                                                                                                                        ~ data = subprocess.check_output(["git", "stash"]).decode("utf-8").split("\n")
                                                                                                                                ~
                                                                                                                                        ~ subprocess.check_output(["git", "pull", "--rebase", "--continue", "origin", "main"]).decode("utf-8").split("\n")
                                                                                                                                                ~ ~ subprocess.check_output(["git", "pull", "--rebase"]).decode("utf-8").split("\n")
                                                                                                                                                        ~ subprocess.check_output(["git", "stash", "pop"]).decode("utf-8").split("\n")
                                                                                                                                                                ~
                                                                                                                                                                        ~
                                                                                                                                                                                ~ pg.sleep(3)
                                                                                                                                                                                        ~ data = subprocess.check_output(["git", "push", "origin", "main"]).decode("utf-8").split("\n")
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        ~ import subprocess
                                                                                                                                                                                        import pyautogui as pg
                                                                                                                                                                                        import os
                                                                                                                                                                                        import PySimpleGUI as sg
                                                                                                                                                                                        from tkinter import messagebox
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        sg.theme("DarkTeal2")
                                                                                                                                                                                        layout = [[sg.T("")], [sg.Text("Select a file to commit: "), sg.Input(key="") , sg.FileBrowse(key="-IN-")], [sg.Text("Select a txt file: "), sg.Input(key="") , sg.FileBrowse(key="-INI-")], [sg.T("")],  [sg.Button("Commit"), sg.Button("Cancel")]]
                                                                                                                                                                                        ~~~Building Window
                                                                                                                                                                                        window = sg.Window('Stedap Commits', layout, icon="sc.ico", size=(600, 200), element_justification="center")
                                                                                                                                                                                        
                                                                                                                                                                                        