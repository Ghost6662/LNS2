from PIL import Image, ImageTk
import datetime
import tkinter as tk

# Creating Window

window = tk.Tk()
window.geometry("350x350")
window.title("Age Calculator App")

# Creating Labels
name_label = tk.Label(text="Name")
name_label.grid(column=0, row=1)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=2)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=3)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=4)

# Creating Entries
name_entry = tk.Entry()
name_entry.grid(column=1, row=1)

year_entry = tk.Entry()
year_entry.grid(column=1, row=2)

month_entry = tk.Entry()
month_entry.grid(column=1, row=3)

day_entry = tk.Entry()
day_entry.grid(column=1, row=4)


def CalculateAge():
    # print(year_entry.get())
    # print(month_entry.get())
    # print(day_entry.get())
    person = Person(name_entry.get(), datetime.date(int(year_entry.get()),
                                        int(month_entry.get()),
                                        int(day_entry.get())))
    answer = tk.Text(master=window, height=10, width=30)
    answer.grid(column = 1, row = 6)
    answer_text = "{name} is {age} years old".format(name=person.name, age=person.age())
    answer.insert(tk.END, answer_text)


# Creating Button
calculate_button = tk.Button(text="Calculate", command=CalculateAge)
calculate_button.grid(column=1, row=5)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


image = Image.open('/Users/ghost/Desktop/LNS/Logo.jpg')
image.thumbnail((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

# Emil = Person("Emil", datetime.date(1995, 11, 06))
# print(Emil.birthdate)
# print(Emil.name)
# print(Emil.age())


window.mainloop()
