import tkinter as tk

root = tk.Tk()

# tk.Widgetname(parent_frame, options)

tk.Entry(root, width=30).pack()

tk.Button(root, text="Button").pack()

tk.Checkbutton(root, text="Done", variable=tk.IntVar).pack()

tk.Label(root, text="This is Label").pack()

tk.OptionMenu(root, tk.IntVar, "Select Age", "18-25", "25-40", "40-60").pack()

tk.Scrollbar(root, orient=tk.VERTICAL).pack()

tk.Radiobutton(root, text="Best", variable=tk.IntVar, value=6).pack()
tk.Radiobutton(root, text="Worst", variable=tk.IntVar, value=3).pack()










root.mainloop()
