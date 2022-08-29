import pgzrun
height=500
width=600
p=Actor("ironman",pos= +(200,200)) ## actor is a image
def draw():
    screen.clear()## self website on net pgzero  
    screen.draw.text("welcome to pgzero",(10,10),color="red",fontsize=50)
    screen.draw.text("created by rafat fatima",(100,100),color="white")
    p.draw()
# outside functions
pgzrun.go()     