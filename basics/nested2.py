from turtle import*
pensize(10)
for i in range(6):
    pencolor("blue")
    fd(100)
    for i in range(4):
         pencolor("red")
         fd(100)
         lt(360/4)
    lt(360/6)
mainloop()    