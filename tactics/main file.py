#author : V-M4K4R0V
#add music , graphics , national anthem
from the_recipe import ask_usr
import turtle
from tkinter import *

background = "/home/o11q/Desktop/git clone/Flying-wedge/tactics/game-map/gamemap.gif"

window = turtle.Screen()
window.title("Flying Wedge")
window.bgpic(background)
window.setup(width=1300, height=800)
#background.s
#window.pensize(24)
#window.stamp()
window.tracer(0)

while True:
    window.update()