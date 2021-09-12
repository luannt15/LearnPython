import turtle
t = turtle
	# Đặt kích thước bút
t.pensize(10)
	# Đặt điểm bắt đầu của hình tròn
t.penup()
t.goto(100,-100)
t.pendown()
	# Nét vẽ là đỏ 
t.pencolor("brown")
	# Nền hình tròn là màu vàng 
t.fillcolor ("blue")
t.begin_fill()
	# Vẽ hình tròn bán kính 100
t.circle(100)
t.end_fill()
t.done()
