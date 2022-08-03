from turtle import*
speed("fastest")
pencolor("green")
bgcolor("yellow")
pensize(20)
side=10
size=100
fillcolor("red")
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)
end_fill()

mainloop()