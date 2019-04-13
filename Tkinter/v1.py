from tkinter import *

window = Tk()
window.title("Welcome to the acanacar app")
# set window size
window.geometry('350x200')

lbl = Label(window, text="Hi")
lbl.grid(column=0, row=0)

# lbl = Label(window, text="Hello", font=("Arial Bold", 50))

txt = Entry(
    window,
    width=10,
    # state='disabled'
)
txt.grid(column=1, row=0)

def clicked():
    res = 'Welcome to ' + txt.get()
    lbl.configure(text=res)


btn = Button(window, text='Click Me', command=clicked)
btn.grid(column=2, row=0)

from tkinter.ttk import *

combo = Combobox(window)

window.mainloop()
