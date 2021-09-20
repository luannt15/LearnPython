# nhập vào bán kính và vẽ hình tròn, tính chu vi, diện tích của hình tròn, hiển thị kết quả ra màn hình
# Bước 1: Nhập bán kính hình tròn 
radius = int(input("nhập vào bán kính của hình tròn: "))
from math import pi 
# Tính chu vi hình tròn 
C = 2 * pi * radius 
print("Chu vi hình tròn là: ",C )
# Tính diện tích hình tròn 
S = pi * radius * radius
print("diện tích hình tròn là: ", S)
import turtle 
t = turtle.Turtle()
t.pensize(5)
t.color("red")
t.circle(radius)
turtle.done()

