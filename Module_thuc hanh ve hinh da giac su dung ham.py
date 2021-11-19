import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor('red')
def draw(n, width=100):
    """Hàm vẽ hình đa giác đều
    n - số cạnh của đa giác đều,
    width - chiều dài của các cạnh
    """
    # Giá trị mỗi góc của đa giác
    t.penup()
    t.pendown()
    angle = (n - 2) * 180 / n
    for i in range(n):
        t.forward(width)
        t.right(180 - angle)

draw(8, 200)

turtle.done()