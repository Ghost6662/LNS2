import tkinter as tk

def write(event):
    print("You wrote a book")
def read(event):
    print("You read a book")

window = tk.Tk()
window.geometry("600x600")

book_label = tk.Label(text = "Books")
book_label.grid(column = 0, row = 0)
Book_button = tk.Button(text = "Read")
Book_button.grid(column = 0, row = 1)

user_label = tk.Label(text = "Emil")
user_label.grid(column = 4, row = 0)
user_button = tk.Button(text = "Write")
user_button.grid(column = 4, row = 1)


user_button.bind("<Button-1>", write)
Book_button.bind("<Button-1>", read)
window.mainloop()