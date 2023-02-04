path = values["-IN-"]
folderpath = values["-INI-"]
print(path)
print(folderpath)

if (path == "" and folderpath == ""):
        messagebox.showinfo(title="info", message="No directory selected")
    elif(folderpath == ""):
            