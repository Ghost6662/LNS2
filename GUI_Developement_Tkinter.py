import tkinter as tk

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

window.mainloop()