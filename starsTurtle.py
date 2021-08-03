import turtle as t
t.speed(0)
t.bgcolor("black")
t.begin_fill()
color = ("red","green","blue","yellow")
for i in range(280):
        t.pencolor(color[i%4])
        t.fillcolor(color[i%4])
        t.begin_fill()
        t.backward(i)
        t.right(100)
        t.end_fill()
        

