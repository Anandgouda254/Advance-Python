from tkinter import *

root = Tk()
root.title("5 Shades of Blue")
root.geometry("600x150")

blue_shades = [
    "#E3F2FD",
    "#90CAF9",
    "#42A5F5",
    "#1E88E5",
    "#0D47A1"
]

for color in blue_shades:
    frame = Frame(root, bg=color, width=120, height=150)
    frame.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()