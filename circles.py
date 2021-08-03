def draw_circle(x,y,color,radius=50):
        t.goto(x,y)
        t.down()
        t.begin_fill()
        t.fillcolor(color)
        t.circle(radius)
        t.end_fill()
        t.up()
        t.home()

import turtle
t = turtle.Turtle()
t.pensize(2)
t.up()
draw_circle(200,200,"Green")
draw_circle(50,-50,"red")
draw_circle(-200,-100,"yellow")
draw_circle(-200,100,"blue")
draw_circle(200,-100,"orange")
draw_circle(200,100,"pink")
draw_circle(-200,200,"skyblue")
draw_circle(200,-200,"purple")
draw_circle(-100,-200,"violet")

