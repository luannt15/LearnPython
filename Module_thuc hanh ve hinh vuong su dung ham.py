import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor('red')
def square_draw(w):
    for i in range(4):
        t.forward(w)
        t.right(90)
    turtle.done()
square_draw(100)