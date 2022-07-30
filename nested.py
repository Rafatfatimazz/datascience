from turtle import *
pensize(5)
speed("slowest")
for i in range(4):
    pencolor("red")
    write(i,font=("arial",14,"normal"),align="left")
    forward(100)
    for i in range(6):
        pencolor("blue")
        fd(100)
        lt(360/6)
    left(360/4)

mainloop()
   