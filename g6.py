import pgzrun

HEIGHT=700
WIDTH=700

class Player(Actor):
    speed=3

    def move(self):
        if keyboard.LEFT and self.left>0:
            self.x+=-self.speed
        if keyboard.RIGHT and self.right<WIDTH:
            self.x+=self.speed

print(dir(Player))
p=Player("player",pos=(100,100))

def draw():
    screen.clear()
    p.draw()
    

def update():
    p.move()    

class Enemy(Actor):
    speed=1
    def chase(self,Player):
        if self.x<Player.x:
            self.x+=self.speed
        if self.x>Player.x:
            self.x+=-self.speed  
              
p=Player("player",pos=(100,100))
e=Enemy("enemy",pos=(400,100))          
def draw():
        screen.clear()
        p.draw()
        e.draw()
def update():
    p.move()
    e.chase(p)
   

pgzrun.go()
            

