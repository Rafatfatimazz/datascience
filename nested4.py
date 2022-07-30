from turtle import*
pensize(10)
speed("fastest")
for i in range(6):
    pencolor("yellow")
    goto(i)
    dot(20)
    fd(100)
    dot(4)
    for i in range(6):
        fd(100)
        pencolor("yellow")
        dot(4)
        lt(360/6)
    lt(360/6)
    
mainloop()    