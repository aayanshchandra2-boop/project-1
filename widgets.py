from tkinter import Button, END, Entry, Label, Text, Tk
from datetime import date

root = Tk()
root.title("getting started with widgets")
root.geometry("400x300")

lbl = Label(text="hey there!", fg="white", bg="#072f5f", height=1, width=300)
name_lbl = Label(text="fullname", bg="#3895D3")
name_entry = Entry()
textbox = Text(height=3)

def display():
    name = name_entry.get()
    greet = "hello " + name + "\n"
    message = "welcome to the application!\nToday's date is: " + str(date.today())
    textbox.delete("1.0", END)
    textbox.insert(END, greet)
    textbox.insert(END, message)

btn = Button(text="begin", command=display, height=1, bg="#1261A0", fg="white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
textbox.pack()

root.mainloop()

    
