import tkinter
import random
from tkinter import *
from tkinter import messagebox

def clicked():
    if txt1.get()!='' and txt2.get()!='':
        res = random.randint(0,100)
        messagebox.showinfo('Результат', 'Вы совместимы на {0}%'.format(res))
    else:
        messagebox.showinfo('Ошибка!',"Заполните оба поля")

window = Tk()
window.title("Посчитай свою любовь")
lbl = Label(window, text="Введи имена двух людей", font=("Comic Sans",30))
lbl.grid(column=0, row=0)
window.geometry('600x250')
txt1 = Entry(window,width=10)
txt1.grid(column=0,row=1)
txt2 = Entry(window,width=10)
txt2.grid(column=1,row=1)
btn = Button(window,text="посчитать",command=clicked)
btn.grid(column=0,row=2)
window.mainloop()
