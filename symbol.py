from turtle import*
speed("fastest")
pencolor("green")
bgcolor("blue")
color("yellow","blue")
pensize(1)
begin_fill()
while True:
    fd(200)
    lt(170)
    if abs(pos())<1:
      break


end_fill()

mainloop()