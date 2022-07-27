from turtle import  *
speed("fastest")
pencolor("black")
pensize(4)
fillcolor("blue")
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()

mainloop()
