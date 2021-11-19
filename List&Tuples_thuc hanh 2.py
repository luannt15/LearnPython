gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,"Television", 1000, "Laptop Case", "Camera Lens"]

# Tạo hai list chứa số và chuỗi từ list đã cho
text = []
numbers = []
for i in gadgets:
    if isinstance(i, str):
        text.append(i)
    else:
        numbers.append(i)
print("List chứa chuỗi = ", text)
print("List chứa số = ", numbers)
# Sắp xếp list chứa chuỗi
text.sort()
print("List chứa chuỗi theo thứ tự tăng dần= ", text)
text.sort(reverse=True)
print("List chứa chuỗi theo thứ tự giảm dần= ", text)
# Sắp xếp list chứa số
numbers.sort()
print("List chứa số theo thứ tự tăng dần= ", numbers)
numbers.sort(reverse=True)
print("List chứa số theo thứ tự giảm dần= ", numbers)