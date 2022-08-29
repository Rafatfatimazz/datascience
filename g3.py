import pgzrun
HEIGHT=500
WIDTH=600
music.play("bg")
p=Actor("ironman",(100,100))
c=Actor("cooki")
c.x= randint(64, WIDTH-64)
c.y= randint(64, HEIGHT-64)
score=0
speed=5
def draw():
    screen.clear()
    screen.fill("pink")
    p.draw()
    c.draw()
    screen.draw.text(f"score:{score}",(WIDTH-80,10))
def update(): 
       player_control()
       update_score()
def update_score():
    global score
    if p.colloiderect(c):
        score+=1
        c.pos=(randint(64,WIDTH64),randint(64,HEIGHT-64)) 
        sounds.eating.play()      
def player_control():

 pgzrun.go()    