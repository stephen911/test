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
                                                                                                