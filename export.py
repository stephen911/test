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
                                
                                        
                                                
                                                