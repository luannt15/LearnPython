import turtle
square = turtle.Turtle()

def draw_square(angle):
    for i in range(3):
        square.forward(100)
        square.right(90)    

    square.forward(100)
    square.right(90 + angle)
    
step = 36
angle = 360 / step
for i in range(step):
    draw_square(angle) 

turtle.done()