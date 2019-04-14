from os import path
from tkinter import *
from tkinter import scrolledtext, messagebox, filedialog, Menu
from tkinter.ttk import *
from tkinter import ttk

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

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, 'Text')
combo.current(1)
combo.grid(column=0, row=1)

# check button
chk_state = BooleanVar()
chk_state.set(True)  # set check state

# chk_state = IntVar()
# chk_state.set(1)  # set check state
# chk_state.set(0)  # set check state
chk = Checkbutton(window, text='Choose')
chk.grid(column=1, row=1)

# radio buttons widgets
rad1 = Radiobutton(window, text='First', value=1)
rad2 = Radiobutton(window, text='Second', value=2)
rad3 = Radiobutton(window, text='Third', value=3)

window2 = Tk()
window2.title("Welcome to the acanacar app")
# set window size
window2.geometry('500x200')

selected = IntVar()
rad1 = Radiobutton(window2, text='First', value=1, variable=selected)
rad2 = Radiobutton(window2, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window2, text='Third', value=3, variable=selected)


def clicked2():
    print(selected.get())
    txt.insert(INSERT, 'You text goes here')


btn = Button(window2, text="Click mee", command=clicked2())
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)
btn.grid(column=3, row=0)
window2.mainloop()

# ScrolledText widget - textarea


window2 = Tk()
window2.title("Welcome to the acanacar app")
# set window size
window2.geometry('500x200')

txt = scrolledtext.ScrolledText(window2, width=40, height=10)
txt.grid(column=0, row=0)


def clicked2():
    txt.insert(INSERT, 'You text goes here')
    messagebox.showinfo('Message title', 'Message content')
    messagebox.showerror('Message title', 'Message content')


btn = Button(window2, text="Click mee", command=clicked2)
btn.grid(column=1, row=0)

# spin = Spinbox(window2, from_=0, to=100, width=5)

var = IntVar()
var.set(3)
spin = Spinbox(window2, values=(3, 5, 8), width=5, textvariable=var)
spin.grid(column=0, row=0)

window2.mainloop()

window3 = Tk()

window3.title('Window 3 title acanacar app')
window3.geometry('500x250')

style = ttk.Style()
style.theme_use('default')
style.configure('black.Horizontal.TProgressbar', background='black')
bar = Progressbar(window3, length=100, style='black.Horizontal.TProgressbar')

bar['value'] = 40
bar.grid(column=0, row=0)
# window3.mainloop()

file = filedialog.askopenfilename()
files = filedialog.askopenfilenames()  # multiple
file = filedialog.askopenfilename(filetypes=(('Text files', "*.txt"), ("all files", "*.*")))  # filter
dir = filedialog.askdirectory()
file = filedialog.askopenfilename(initialdir=path.dirname(__file__))


def hello():
    print('hello')


menu = Menu(window3)

new_item = Menu(menu)
new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)
menu.add_command(label='Quit!', command=window3.quit)
menu.add_command(label='Hi!', command=hello)
window3.config(menu=menu)

window3.mainloop()

window4 = Tk()

window4.title('Notebook acanacar')

tab_control = ttk.Notebook(window4)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text='Label1', padx=5, pady=5)
lbl1.grid(columns=1, row=1)
lbl2 = Label(tab2, text='Label2', padx=5, pady=5)
lbl2.grid(columns=2, row=0)

tab_control.pack(expand=1, fill='both')

window4.mainloop()
