num = int(input("Nhập vào đơn giá: "))
if num >= 150:
	print("Tổng số tiền phải trả: ", num - 50)
elif num >= 100:
	print("Tổng số tiền phải trả", num - 25)
elif num >= 75:
	print("Tổng số tiền phải trả", num - 15)
else:
print("Tổng số tiền phải trả ", num)