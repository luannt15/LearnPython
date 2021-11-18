import random

class flashcard:
    def __init__(self):

        self.fruits = {	'trái bơ': 'avocado',
                        'trái me': 'tamarind',
                        'trái bưởi': 'pomelo',
                        'trái mơ': 'apricot',
                        'trái hồng': 'persimmon',
                        'trái na': 'custard apple',
                        'trái đu đủ': 'papaya'}

    def quiz(self):
        while True:

            vietnamese, english = random.choice(list(self.fruits.items()))

            print("Tiếng Anh của '{}' là: ".format(vietnamese))
            user_answer = input()

            if user_answer.lower() == english:
                print("Đúng")
            else:
                print("Sai")

            option = int(input("Nhập 0 để tiếp tục : "))
            if option:
                break
        print("Kết thúc")
fc = flashcard()
fc.quiz()