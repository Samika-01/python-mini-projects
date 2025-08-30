from tkinter import *

root = Tk()

root.title("Welcome to my GUI")
root.geometry('400x200')


menu = Menu(root)
item = Menu(menu)
item.add_command(label = "New")
menu.add_cascade(label="File", menu= item)
root.config(menu = menu)

lb1 = Label(root, text="hello there!")
lb1.grid()


txt = Entry(root, width=20)
txt.grid(column=1, row=0)

def clicked():
    res = "You wrote " + txt.get()
    lb1.configure(text=res)

btn = Button(root, text="Click me", fg="red" , command=clicked)
btn.grid(column=2, row=0)

root.mainloop()