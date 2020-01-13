#author : V-M4K4R0V
#add music , graphics , national anthem
from the_recipe import ask_usr
from countries import world_map
from age import comrade_age
from tkinter import *

root=Tk()

canvas = Canvas(width=1400, height=900, bg='blue')
background = PhotoImage(file="C:\\Users\\ahmed\\Desktop\\work\\Flying-wedge\\tactics\\game-map\\new-map.png")
canvas.create_image(0,0, image=background, anchor=NW)
canvas.pack()

root.mainloop()