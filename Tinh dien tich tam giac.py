import math
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a <= 0 or b <= 0 or c <= 0 or a+b<=c or a+c<=b or c+b<=a : 
	print("Nhập sai dữ liệu") 
else: 
	# nửa chu vi 
	p = (a+b+c)/2
	# Diện tích tam giác
	DT = math.sqrt(p*(p-a)*(p-b)*(p-c))
	print(" Dien tich tam giac la: ", DT)
