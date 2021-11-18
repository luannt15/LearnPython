chieu_cao = float(input("Nhập chiều cao của bạn(m): "))
can_nang = float(input("Nhập cân nặng của bạn(kg): "))
BMI = can_nang/(chieu_cao**2)

if BMI < 16:
	print("Gầy cấp độ III")
elif 16 <= BMI < 17:
	print("Gầy cấp độ II")
elif 17<= BMI < 18.5:
	print("Gầy cấp độ I")
elif 18.5 <= BMI < 25:
	print("Bình thường")
elif 25 <= BMI < 30:
	print("Thừa cân")
elif 30 <= BMI < 35:
	print("Béo phì cấp độ I")
elif 35 <= BMI < 40:
	print("Béo phì cấp độ II")
elif 40 <= BMI:
	print("Béo phì cấp độ III")
