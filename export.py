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
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        def push():
                                                                                                                                                                                    path = values["-IN-"]
                                                                                                                                                                                        folderpath = values["-INI-"]
                                                                                                                                                                                            print(path)
                                                                                                                                                                                                print(folderpath)
                                                                                                                                                                                                    
                                                                                                                                                                                                        if (path == "" and folderpath == ""):
                                                                                                                                                                                                                
                                                                                                                                                                                                                        messagebox.showinfo(title="info", message="No directory selected")
                                                                                                                                                                                                                    elif(folderpath == ""):
                                                                                                                                                                                                                                    messagebox.showinfo(title="info", message="Please select file path to commit from")
                                                                                                                                                                                                                                elif(path == ""):
                                                                                                                                                                                                                                                messagebox.showinfo(title="info", message="Please select file to commit")
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               