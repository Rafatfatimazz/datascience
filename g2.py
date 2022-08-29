import pgzrun
HEIGHT=500
WIDTH=600

p=Actor("ironman",(100,100))
speed=3
def draw():
    screen.clear()
    p.draw()
def update():
    print("updating") 
    if keyboard.RIGHT:## press right arow to move it from left to right
        p.x+=speed   

pgzrun.go()    