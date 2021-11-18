import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor("blue")
edge = 0
while edge < 4:
    t.forward(100)
    t.right(90)
    edge += 1
turtle.done()