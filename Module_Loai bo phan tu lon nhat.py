numbers = [1, 2, 66, 22, 45, 33, 3]

def remove_largest_number(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    numbers.remove(largest)


remove_largest_number(numbers)
print(numbers)