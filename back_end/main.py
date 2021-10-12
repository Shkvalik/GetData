import re
from tkinter import messagebox, filedialog
import pyperclip
import requests
from tkinter import *
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema
from back_end.forms import FORMS


def get_data(link, t_form):
    try:
        url = BeautifulSoup(requests.get(link).text, 'lxml')
        print(url)
    except MissingSchema:
        return messagebox.showerror("Error", "Вы ввели некоректную форму ссылки")
    cloud = []
    result = []
    try:
        for form in FORMS[t_form]:
            data = re.findall(form, str(url))
            cloud += data
            # print(f'{form}-->{data}')
        if cloud:
            for a in cloud:
                if a in result:
                    continue
                else:
                    result.append(a)

            return result
        else:
            return messagebox.showinfo('Info' ,'К сожалению, ничего не нашлось')
    except KeyError:
        return messagebox.showerror("Error", 'Вы не выбрали тип сбора данных')


def save_data(result):
    try:
        ask_q_show = messagebox.askquestion('Info', f'Готово! Было найдено: {len(result)}. Показать?')
        if ask_q_show == 'yes':
            ask_q_save = messagebox.askquestion('Info', f'{result}\nСохранить?')
            if ask_q_save == 'yes':
                file_name = filedialog.asksaveasfilename(
                    filetypes=(("TXT files", "*.txt"),
                               ("CSV files", "*.csv")))
                if file_name:
                    with open(file_name, 'w+') as f:
                        for d in result:
                            f.write(d + "\n")
                    messagebox.showinfo('Info', "Ура-ура! Это успех!")
    except FileNotFoundError:
        messagebox.showerror('Error', 'Упс! Кажись что-то пошло не так...')