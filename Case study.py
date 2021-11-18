import turtle 

t = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("white")
t.speed(0)

# Ve khung ngoài bức tranh
def khung_bao_ngoai():
    t.pensize(4)
    t.penup()
    t.goto(0,320)
    t.pendown()
    t.forward(600)
    t.right(90)
    t.forward(640)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(640)
    t.right(90)
    t.forward(600)

# Họa tiết góc
def hoa_tiet_goc():
    t.fillcolor("brown")
    t.begin_fill()
    t.forward(35)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(35)
    t.end_fill()

# Họa tiết chữ S
def hoa_tiet_chu_S():
    t.fillcolor("brown")
    t.begin_fill()
    t.forward(35)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.end_fill()

# Khung hoa văn góc trái phía trên 
def khung_hoa_van_trai_tren():
    # Họa tiết góc vuông trái phía trên
    t.setheading(90)
    t.penup()
    t.goto(-590,310)
    t.pensize(1)
    t.pendown()
    t.right(90)
    hoa_tiet_goc()

    # 6 ký tự ngang
    t.right(90)
    i = 0
    for x in range(6):
        t.setheading(90)
        t.right(90)
        t.penup()
        t.goto(-520+i,310)
        t.pendown()
        hoa_tiet_chu_S()
        i = i+70

    # 1 ký tự dọc
    t.penup()
    t.goto(-130,215)
    t.pendown()
    hoa_tiet_chu_S()

    # Vẽ nét chéo
    t.left(45)
    t.penup()
    t.goto(-115,190)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()

    # 3 ký tự dọc
    j = 0
    for x in range(3):
        t.penup()
        t.setheading(90)
        t.goto(-590,175-j)
        t.pendown()
        hoa_tiet_chu_S()
        j = j+70
        t.right(90)

    # 4 ký tự ngang 
    k = 0 
    for x in range(4):
        t.setheading(90)
        t.right(90)
        t.penup()
        t.goto(-560+k,60)
        t.pendown()
        hoa_tiet_chu_S()
        k = k+70 

# Khung hoa văn góc phải phía trên
def khung_hoa_van_phai_tren():
    # Họa tiết góc phải phía trên
    t.penup()
    t.goto(590,310)
    t.pensize(1)
    t.pendown()
    t.right(-180)
    hoa_tiet_goc()

    # 6 ký tự ngang
    i = 0
    for x in range(6):
        t.setheading(90)
        t.right(90)
        t.penup()
        t.goto(455-i,310)
        t.pendown()
        hoa_tiet_chu_S()
        i = i+70

    # 1 ký tự dọc
    t.penup()
    t.goto(105,215)
    t.pendown()
    hoa_tiet_chu_S()

    # 3 ký tự chéo
    t.penup()
    t.goto(132,208)
    t.left(135)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()

    # 3 ký tự dọc 
    j = 0
    for x in range(3):
        t.setheading(90)
        t.penup()
        t.goto(565,175-j)
        t.pendown()
        hoa_tiet_chu_S()
        j = j+70
        t.right(90)

    # 4 ký tự ngang 
    k = 0 
    for x in range(4):
        t.setheading(90)
        t.right(90)
        t.penup()
        t.goto(495-k,60)
        t.pendown()
        hoa_tiet_chu_S()
        k = k+70 
 
# Khung hoa văn góc phải phía dưới
def khung_hoa_van_phai_duoi():
    # Họa tiết góc phải phía dưới
    t.penup()
    t.goto(590,-310)
    t.pensize(1)
    t.pendown()
    t.left(90)
    hoa_tiet_goc()
    
    # 6 ký tự ngang
    i = 0
    for x in range(6):
        t.setheading(90)
        t.right(90)
        t.penup()
        t.goto(455-i,-285)
        t.pendown()
        hoa_tiet_chu_S()
        i = i+70

    # 1 ký tự dọc
    t.penup()
    t.goto(105,-280)
    t.pendown()
    hoa_tiet_chu_S()

    # 3 ký tự chéo 
    t.penup()
    t.goto(114,-194)
    t.left(225)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()

    # 3 ký tự dọc
    j = 0
    for x in range(3):
        t.setheading(90)
        t.penup()
        t.goto(565,-240+j)
        t.pendown()
        hoa_tiet_chu_S()
        j = j+70
        t.right(90)

    # 4 ký tự ngang 
    k = 0 
    for x in range(4):
        t.setheading(90)
        t.right(90)
        t.penup()
        t.goto(495-k,-35)
        t.pendown()
        hoa_tiet_chu_S()
        k = k+70 
    
# Khung hoa văn góc trái phía dưới
def khung_hoa_van_trai_duoi():
    # Họa tiết góc trái phía dưới
    t.penup()
    t.goto(-590,-310)
    t.pensize(1)
    t.pendown()
    hoa_tiet_goc()

    # 6 ký tự ngang
    i = 0
    for x in range(6):
        t.setheading(90)
        t.right(90)
        t.penup()
        t.goto(-520+i,-285)
        t.pendown()
        hoa_tiet_chu_S()
        i = i+70

    # 1 ký tự dọc
    t.penup()
    t.goto(-130,-280)
    t.pendown()
    hoa_tiet_chu_S()

    # 3 ký tự chéo
    t.penup()
    t.goto(-130,-210)
    t.left(-45)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()
    t.penup()
    t.right(90)
    t.forward(70)
    t.pendown()
    hoa_tiet_chu_S()
    
    # 3 ký tự dọc
    j = 0
    for x in range(3):
        t.setheading(90)
        t.penup()
        t.goto(-590,-240+j)
        t.pendown()
        hoa_tiet_chu_S()
        j = j+70
        t.right(90)

    # 4 ký tự ngang 
    k = 0 
    for x in range(4):
        t.setheading(90)
        t.left(90)
        t.penup()
        t.goto(-495+k,-60)
        t.pendown()
        hoa_tiet_chu_S()
        k = k+70 

# Class hoa với các thuộc tính: chiều dài cánh hoa, màu sắc cánh hoa, số lượng cánh hoa
class hoa():
    def __init__(self, r, mau, n):
        """
        Hàm khởi tạo có tham số
        r: chiều dài cánh hoa
        mau: Màu sắc
        n: số lượng
        """
        self.r = r
        self.mau = mau
        self.n = n 

    def ve_bong_hoa(self):
        t.fillcolor(self.mau)
        t.begin_fill()
        for i in range(self.n):
            t.setheading(0)
            t.right(360/self.n*i)
            t.circle(self.r,90)
            t.left(90)
            t.circle(self.r,90)
        t.end_fill()

hoa_hoa_tiet_phu = hoa(15,"yellow", 6)
hoa_hoa_tiet_chinh = hoa(150,"pink", 8)

# Hoa tiet goc trái trên
def hoa_tiet_hoa_goc_trai_tren():
    t.setheading(0)
    t.right(35)
    t.penup()
    t.goto(-550,280)
    t.pendown()
    t.circle(180,60)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(-550,280)
    t.pendown()
    t.setheading(0)
    t.right(30)
    t.circle(180,30)
    t.left(180)
    t.circle(220,-50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.setheading(0)
    t.right(50)
    t.circle(-220,-25)
    t.circle(220,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(-550,280)
    t.pendown()
    t.setheading(0)
    t.right(50)
    t.circle(-180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(-550,280)
    t.pendown()
    t.setheading(0)
    t.right(50)
    t.circle(180,25)
    t.circle(-180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()

# Hoa tiet goc trái dưới
def hoa_tiet_hoa_goc_trai_duoi():
    t.setheading(0)
    t.left(35)
    t.penup()
    t.goto(-550,-280)
    t.pendown()
    t.circle(-180,60)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(-550,-280)
    t.pendown()
    t.right(-60)
    t.circle(-180,30)
    t.left(180)
    t.circle(-220,-50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.left(80)
    t.circle(220,-25)
    t.circle(-220,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(-550,-280)
    t.pendown()
    t.right(-80)
    t.circle(180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(-550,-280)
    t.pendown()
    t.left(80)
    t.circle(-180,25)
    t.circle(180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()

# Hoa tiet goc phải trên 
def hoa_tiet_hoa_goc_phai_tren():
    t.setheading(0)
    t.right(145)
    t.penup()
    t.goto(550,280)
    t.pendown()
    t.circle(-180,60)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(550,280)
    t.pendown()
    t.setheading(0)
    t.right(150)
    t.circle(-180,30)
    t.left(180)
    t.circle(-220,-50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.right(100)
    t.circle(220,-25)
    t.circle(-220,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(550,280)
    t.pendown()
    t.setheading(0)
    t.right(130)
    t.circle(180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(550,280)
    t.pendown()
    t.left(-100)
    t.circle(-180,25)
    t.circle(180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()

# Hoa tiet goc phải dưới
def hoa_tiet_hoa_goc_phai_duoi():
    t.setheading(0)
    t.left(145)
    t.penup()
    t.goto(550,-280)
    t.pendown()
    t.circle(180,60)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(550,-280)
    t.pendown()
    t.setheading(0)
    t.left(150)
    t.circle(180,30)
    t.left(180)
    t.circle(220,-50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.left(160)
    t.circle(-220,-25)
    t.circle(220,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(550,-280)
    t.pendown()
    t.right(200)
    t.circle(-180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()
    t.penup()
    t.goto(550,-280)
    t.pendown()
    t.right(205)
    t.circle(180,25)
    t.circle(-180,50)
    hoa_hoa_tiet_phu.ve_bong_hoa()    


khung_bao_ngoai()

khung_hoa_van_trai_tren()
khung_hoa_van_phai_tren()
khung_hoa_van_phai_duoi()
khung_hoa_van_trai_duoi()

hoa_tiet_hoa_goc_trai_tren()
hoa_tiet_hoa_goc_trai_duoi()
hoa_tiet_hoa_goc_phai_tren()
hoa_tiet_hoa_goc_phai_duoi()

# Ve hoa tiet chinh 
t.penup()
t.goto(0,0)
t.pendown()

hoa_hoa_tiet_chinh.ve_bong_hoa()

t.hideturtle()
turtle.done()
