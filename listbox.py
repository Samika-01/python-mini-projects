from tkinter import *

root = Tk()
root.title("Programming Languages")
root.geometry("400x200")
lb = Listbox(root)
lb.insert(1, "Python") 
lb.insert(2, "Java")
lb.insert(3, "JavaScript")
lb.insert(4, "C")
lb.insert(5,"any other")

lb.grid(row=0)
root.mainloop()
