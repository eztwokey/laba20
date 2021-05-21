#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

#   Решите задачу:
#   Напишите программу, состоящую из двух списков Listbox.
#   В первом будет, например, перечень товаров, заданный программно.
#   Второй изначально пуст, пусть это будет перечень покупок.
#   При клике на одну кнопку товар должен переходить из одного списка в другой.
#   При клике на вторую кнопку – возвращаться (человек передумал покупать).
#   Предусмотрите возможность множественного выбора элементов списка и их перемещения.


# Создаем функцию для перемещения вперед
def add_item():
    product = []
    select = list(lbox_first.curselection())
    select.reverse()
    for i in select:
        op = lbox_first.get(i)
        product.append(op)
    for val in product:
        # print(val)
        lbox_second.insert(0, val)
        # lbox_first.delete(val)
    for k in select:
        lbox_first.delete(k)


# Создаем функцию для перемещения назад
def delete_item():
    product = []
    select = list(lbox_second.curselection())
    select.reverse()
    for i in select:
        op = lbox_second.get(i)
        product.append(op)
    for val in product:
        # print(val)
        lbox_first.insert(0, val)
        # lbox_first.delete(val)
    for k in select:
        lbox_second.delete(k)


if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Персонажи')
    root.geometry('364x200')

    # Создаем список продуктов
    products = ['Pudge', 'Puck', 'Enchantress', 'Spirit Breaker', 'Tidehunter', 'SF', 'Mirana', 'Enigma', 'Void Spirit', 'ICE FROG']

    # Создаем списки с помощью интерфейса
    lbox_first = Listbox(selectmode=EXTENDED)
    lbox_second = Listbox(selectmode=EXTENDED)

    # Создаем кнопки для выполнений определенных команд
    button_up = Button(height=1, width=5, text='>>>>', command=add_item)
    button_back = Button(height=1, width=5, text='<<<<', command=delete_item)

    # Выводим
    lbox_first.grid(row=1, column=1, pady=15, padx=3)
    lbox_second.grid(row=1, column=4, pady=15)

    button_up.grid(row=1, column=2, padx=3)
    button_back.grid(row=1, column=3, padx=5)

    # Выводим данные в наш список(виджет)
    for i in products:
        lbox_first.insert(END, i)

    # Запуск программы
    root.mainloop()