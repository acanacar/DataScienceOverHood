from tkinter import *

window = Tk()
window.title("Welcome to the acanacar app")
# set window size
window.geometry('500x200')

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

# combobox widget
from tkinter.ttk import *

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, 'Text')
combo.current(1)
combo.grid(column=0, row=1)

# check button
chk_state = BooleanVar()
chk_state.set(True)  # set check state
# chk_state.set(1)  # set check state
# chk_state.set(0)  # set check state
chk = Checkbutton(window, text='Choose')
chk.grid(column=1, row=1)

# radio buttons widgets

rad1 = Radiobutton(window, text='First', value=1)
rad2 = Radiobutton(window, text='Second', value=2)
rad3 = Radiobutton(window, text='Third', value=3)

rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)

window.mainloop()

window.mainloop()
