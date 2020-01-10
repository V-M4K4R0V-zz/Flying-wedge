import turtle

def the_map():
    
    window = turtle.Screen()
    window.title("Flying Wedge")
    window.bgpic("/home/o11q/Desktop/git clone/Flying-wedge/tactics/game-map/gamemap.gif")
    window.setup(width=1300, height=800)
    #window.tracer(0)
    while True:
        window.update()