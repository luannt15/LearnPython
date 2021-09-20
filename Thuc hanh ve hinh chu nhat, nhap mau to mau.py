import turtle
t=turtle 
color_code = input("Enter color code: ")
Length = float(input("length of rectangle: "))
Width = float(input("Width of rectangle: "))
# Tinh chu vi hinh chu nhat 
C = 2 * ( Length + Width)
print("Chu vi hinh chu nhat la: ", C)
# Tinh dien tich hinh chu nhat
S = Length * Width 
print("Dien tich hinh chu nhat la: ", S)
t.begin_fill()
t.fillcolor(color_code)
t.penup()
t.pendown()
t.forward(Length)
t.right(90)
t.forward(Width)
t.right(90)
t.forward(Length)
t.right(90)
t.forward(Width)
t.right(90)
t.end_fill()
t.done()

