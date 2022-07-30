from turtle import*
pensize(10)
for i in range(6):
    pencolor("yellow")
    fd(100)
    for i in range(6):
        pencolor("green")
        fd(100)
        lt(360/6)
    lt(360/6)
mainloop()        