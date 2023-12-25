import tkinter as tk
from tkinter import Label

import pygame
import random
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("The Sims 4 — Soundtrack.mp3")


def key():
    hex = ''
    block4 = ''
    letters = '1234567890ABCDEF'
    for i in range(5):
        hex += random.choice(letters)
    dec = int(hex, 16)
    a = str(dec)
    block1 = a[0]
    block2 = a[1]
    block3 = a[2]
    for i in range(4):
        block1 += random.choice(letters)
        block2 += random.choice(letters)
        block3 += random.choice(letters)
    block4 = a[-1] + a[-2]
    temp_key = block1 + '-' + block2 + '-' + block3 + ' ' + block4
    return temp_key


def animation():
    for i in range(10):
        window.update_idletasks()

        frame = tk.Frame(window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        label_bg: Label = tk.Label(frame, image=bg)
        label_bg.grid()

        label_animation = tk.Label(frame, text=key(), font=("Arial", 30), bg='#999900')
        label_animation.grid(column=0, row=0, padx=10, pady=20)

        time.sleep(0.5)


window = tk.Tk()
window.title("Astroneer key generator")
window.geometry('750x1000')
bg = tk.PhotoImage(file='the-sims-4.png')

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

label_bg = tk.Label(frame, image=bg)
label_bg.grid()

button_key = tk.Button(frame, text='Сгенерировать уникальный код', font=("Arial", 15), command=animation)
button_key.grid(column=0, row=0, padx=10, pady=20)

pygame.mixer.music.play(-1)
window.mainloop()