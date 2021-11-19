products = {
            'SMART WATCH': 550,
            'PHONE' : 1000,
            'PLAYSTATION': 500,
            'LAPTOP' : 1550,
            'MUSIC PLAYER' : 600,
            'TABLET' : 400 
           }

def display_product(products_db, price):
    for item in products_db:
        if products_db[item] <= price:
            print(item, " : ",products_db[item])
    
input_price = int(input("Enter the price :"))

display_product(products, input_price)