import turtle

#creating turtle background color using bg

turtle.bgcolor("black")

#setting pensize
turtle.pensize(2)

#setting speed
turtle.speed(0)

for i in range(6):
        for colors in ["red","blue","green","purple","pink","yellow","violet","cyan","magenta"]:
                turtle.color(colors)
                turtle.circle(100)
                turtle.left(10)

turtle.hideturtle()
