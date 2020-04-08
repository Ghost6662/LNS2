import tkinter as tk
import webbrowser

URL = "https://youtube.com"

def openYoutube(event):
    webbrowser.open_new_tab(URL)

def BestSong(event):
    webbrowser.open_new_tab(URL + "/watch?v=Z7Y3r_st5Do")

window = tk.Tk()

window.geometry("300x400")

alabel = tk.Label(text="Yutube")
alabel.grid(column=0, row=0)

button1 = tk.Button(text="Enter Youtube")
button1.grid(column=0 ,row=1)

button1.bind("<Button-1>",openYoutube)


blabel = tk.Label(text="Best Song")
blabel.grid(column=1, row=0)

button2 = tk.Button(text="Play the Best Song")
button2.grid(column=1, row=1)
button2.bind("<Button-1>", BestSong)

window.mainloop()