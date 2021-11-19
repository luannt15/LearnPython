import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Square")

myPen = turtle.Turtle()
myPen.speed(2)
myPen.color("green")

for i in range(4):
  myPen.forward(100)
  myPen.left(90)

turtle.done()