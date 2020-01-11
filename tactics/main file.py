#author : V-M4K4R0V
#add music , graphics , national anthem
from the_recipe import ask_usr
from countries import world_map
from age import comrade_age
from tkinter import *
from PIL import ImageTK,Image

background = "/home/o11q/Desktop/git clone/Flying-wedge/tactics/game-map/gamemap.gif"

root=Tk()

convas=convas(root,width=1200,height=800)
image=ImageTK.PhotoImage(Image.open(background))

convas.create_image(0,0,anchor=NW,image=image)
convas.pack()

root.mainloop()