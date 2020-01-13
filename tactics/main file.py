#author : V-M4K4R0V
#add music , graphics , national anthem
from the_recipe import ask_usr
from countries import world_map
from age import comrade_age
from about import about_game
from tkinter import *

#window
root = Tk()
def hello():
    print("welcome Player!")

menubar = Menu(root)

#File button
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# create more pulldown menus // edit button
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)

#help button
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_game)


# display the menu
root.config(menu=menubar)

#map
canvas = Canvas(width=1366, height=768, bg='blue')
background = PhotoImage(file="C:\\Users\\ahmed\\Desktop\\work\\Flying-wedge\\tactics\\game-map\\new-map.png")
canvas.create_image(0,0, image=background, anchor=NW)
canvas.pack()
#game loop
root.mainloop()