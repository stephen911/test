~ pg.sleep(3)
~ pg.write("git push origin main")
~ pg.press("enter")
while True:
            event, values = window.read()
                if event == sg.WIN_CLOSED or event == "Exit":
                                break
                        