import pgzrun
HEIGHT=500
WIDTH=600

p=Actor("ironman",(100,100))
speed=5
def draw():
    screen.clear()
    p.draw()
def update():
    print("updating") 
    if keyboard.UP:## press right arow to move it from left to right
        p.x+=-speed   
    if keyboard.DOWN:
        p.x+=speed   
    

pgzrun.go()    