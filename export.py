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
                                                                                                                                                                                                                               