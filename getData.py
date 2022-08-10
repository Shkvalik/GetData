from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from back_end.main import get_data, save_data
from back_end.forms import FORMS

def about():
    messagebox.showinfo('Info', 'Написать автору:\nTelegram:@Shkvalik\n \nПоддежрать автора:\n5375 4141 2301 6940')


def click():
    result = get_data(link.get(), combo.get())
    if result != 'ok':
        save_data(result)


###################################### Window ##########################################################################
window = Tk()
window.title("GetData by Shkvalik(beta 0.1)")
window.update_idletasks()
s = window.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_root // 2
h = h - height_root // 2
window.geometry('+{}+{}'.format(w, h))
window.resizable(False, False)
###################################### Content ##########################################################################
lbl = Label(window, text="Введите адресс сайта")
link = Entry(window, width=50)
combo = Combobox(window, values=list(FORMS.keys()))
btn = Button(window, text="Запуск", command=click, bg="black", fg="white")
abtn = Button(window, text="💡", command=about)
######################################
lbl.pack()
link.pack(fill='x')
combo.pack()
btn.pack()
abtn.pack()
window.mainloop()
