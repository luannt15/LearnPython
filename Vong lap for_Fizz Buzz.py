so_bat_dau = int(input("nhập vào số đầu: "))
so_ket_thuc = int(input("nhập vào số cuối: "))

if so_bat_dau > so_ket_thuc:
    print("Nhập sai, số đầu phải lớn hơn số cuối")
else:

    for i in range(so_bat_dau,so_ket_thuc):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz") 
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

