#author : V-M4K4R0V
#add music , graphics , national anthem
from the_recipe import ask_usr
from countries import world_map
from age import comrade_age
from tkinter import *

#window
root = Tk()
def hello():
    print("welcome comrad")

# create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=root.quit)

# display the menu
root.config(menu=menubar)

#map
canvas = Canvas(width=1366, height=768, bg='blue')
background = PhotoImage(file="C:\\Users\\ahmed\\Desktop\\work\\Flying-wedge\\tactics\\game-map\\new-map.png")
canvas.create_image(0,0, image=background, anchor=NW)
canvas.pack()
#user info
#ask_usr(nana)
#Coordinates
#Coordinates = look for a Coordinates LIB
#world_map(coordinates)

root.mainloop()