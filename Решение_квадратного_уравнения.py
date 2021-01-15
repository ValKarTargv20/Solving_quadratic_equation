from tkinter import *
from math import*
from random import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
a=randint(-10,10)
b=randint(-10,10)
c=randint(-10,10)
D = b*2 - 4*a*c
if D > 0:
    x1 = -b - sqrt(D)/2*a
    x2 = -b + sqrt(D)/2*a
    answer=f'Первый х = {x1} \nВторой х = {x2}'
elif D==0:
    x3 = -b/2*a
    answer=f'В данном уравнении только один корень = {x3}, так как «D = 0»'
else:
    answer=f'B квадратном уравнении нет корней, когда «D < 0» '
def lkm(event):
    global a,b,c,D
    lbl.configure(text=f'Квадратное уравнение \n ax^2+bx+c=0 \nЧисло а = {a}\nЧисло b = {b}\nЧисло c = {c}\nДискриминант ={D} \n{answer}')
x=[i for i in range (-10,11,1)]
y=[(-2*i**2)+(3*i)+2 for i in x]
def pic_to_lkm (event):
    global x,y
    plt.subplots()
    plt.title("График квадратичной функции $ax^2+bx+c=0$")
    plt.xlabel("Y")
    plt.ylabel("X")
    plt.grid(True)
    plt.plot(x, y, marker='o')
    plt.show()

win=Tk() 
win.title('Решение квадратного уравнения')
win.geometry('500x1000')
btn=Button(win,text="Нажми на меня \nи я решу \nквадратное \nуравнение",fg="blue",bg="lightblue",font="Arial 12", width=15) #,command=disc)
lbl=Label(win,text="",fg="blue",bg="lightblue",font="Arial 12")
btn2=Button(win,text="Нажми на меня \nи я построю \nграфик функции",fg="blue",bg="lightblue",font="Arial 12", width=15)
#lbl2=Label(win,text="",fg="blue",bg="lightblue",font="Arial 12")
btn.bind("<Button-1>",lkm)
btn2.bind("<Button-1>",pic_to_lkm)
btn.pack()
lbl.pack()
btn2.pack()
#lbl2.pack()
win.mainloop()



