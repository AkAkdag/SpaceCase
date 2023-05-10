from tkinter import *
import eindopdracht
import opdracht6_AKAR



# Maak een nieuw window met een titel
window = Tk()
window.title("Menu voorbeeld")

# Functies voor het menu
def show_thing_1():
    frame_Senn.pack_forget()
    frame_akkar.pack_forget()
    frame_thing_4.pack_forget()
    frame_thing_1.pack()

def show_frame_Senn():
    frame_Senn.pack()
    frame_thing_1.pack_forget()
    frame_akkar.pack_forget()
    frame_thing_4.pack_forget()

def show_frame_Akkar():
    frame_akkar.pack()
    frame_thing_1.pack_forget()
    frame_Senn.pack_forget()
    frame_thing_4.pack_forget()

def show_thing_4():
    frame_thing_4.pack()
    frame_thing_1.pack_forget()
    frame_Senn.pack_forget()
    frame_akkar.pack_forget()

# Menu maken
menubar = Menu(window)
window.config(menu=menubar)

# Menu items maken
mainmenu = Menu(menubar)
mainmenu.add_command(label="Thing 1", command=show_thing_1)
mainmenu.add_command(label="Frame Senn", command=show_frame_Senn) 
mainmenu.add_command(label="Thing 3", command=show_frame_Akkar)
mainmenu.add_command(label="Thing 4", command=show_thing_4)         
mainmenu.add_separator()
mainmenu.add_command(label="Exit", command=window.quit)
# Menu toevoegen aan menubar
menubar.add_cascade(label="Tool", menu=mainmenu)

# FRAME VOOR THING 1 --------------------------------
frame_thing_1 = Frame(borderwidth=10)
label_1 = Label(frame_thing_1, text="THING 1", bg = "blue", fg="white", width=20, height=8)
label_1.pack()


# FRAME VOOR THING 2 --------------------------------
# eindopdrachtSenn = eindopdracht.tekenen(Frame(borderwidth=10))
frame_Senn = Frame(borderwidth=10)
test = eindopdracht.tekenen(frame_Senn)
frame_Senn = test.returnFrame()



# FRAME VOOR THING 3 --------------------------------
# frame_akkar = opdracht6_AKAR.Application(window)
frame_akkar = Frame(borderwidth=10)


# FRAME VOOR THING 4 --------------------------------
frame_thing_4 = Frame(borderwidth=10)

# MAIN --------------------------------
# Begin met frame 1
show_thing_1()
# Start the application
window.mainloop()
