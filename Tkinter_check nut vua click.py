from tkinter import *
  
app = Tk()

def apple_button_click():
   print("It is an apple")

def banana_button_click():
   print("It is an banana")

b1 = Button(app, text="Apple", command=apple_button_click)
b1.grid(padx=10, pady=10)  

b2 = Button(app, text="Banana", command=banana_button_click)
b2.grid(padx=10, pady=10)

app.mainloop()