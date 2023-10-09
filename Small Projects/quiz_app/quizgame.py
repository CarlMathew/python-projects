from tkinter import *
from PIL import Image, ImageTk
import requests
import random
import os
import pygame
import time
import html
my_api = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
my_api.raise_for_status()
quiz = my_api.json()["results"][0]
question = html.unescape(quiz["question"])
points = 0
window = Tk()
window.geometry("500x500")
window.configure(background="#AE445A")
answer = ""
true_list = os.listdir("true_sound")
false_list = os.listdir("false_sound")
color_back = "white"
def play(sound_file):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
def hatdog():
    mycanvas.configure(background="white")

score_label = Label(text="Score: ", font=("Roboto", 12, "normal"), background="#AE445A")
score_label.place(x=225, y=0)
user_score = Label(text=0, font=("Roboto", 12, "normal"), background="#AE445A")
user_score.place(x=273, y=0)
mycanvas = Canvas(height=300, width=400, background=color_back)
question_api = mycanvas.create_text(200, 150, text=question, fill="black",
                                              width=250, justify="center", font=("Roboto", 15, "italic"))
mycanvas.place(x=50, y=45)
def true_value():
    global quiz, answer, points,question_api,my_api, color_back
    answer = "True"
    if quiz["correct_answer"] == answer:
        points += 1
        user_score.configure(text=points)
        my_api = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
        my_api.raise_for_status()
        mycanvas.configure(background="green")
        window.after(1000, hatdog)
        quiz = my_api.json()["results"][0]
        question = html.unescape(quiz["question"])
        mycanvas.itemconfig(question_api, text= question)
        play(f"true_sound/{random.choice(true_list)}")
    elif quiz["correct_answer"] != answer:
        my_api = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
        my_api.raise_for_status()
        quiz = my_api.json()["results"][0]
        mycanvas.configure(background="red")
        window.after(1000, hatdog)
        question = html.unescape(quiz["question"])
        mycanvas.itemconfig(question_api, text=question)
        play(f"false_sound/{random.choice(false_list)}")
def false_value():
    global quiz, answer, points,question_api,my_api
    answer = "False"
    if quiz["correct_answer"] == answer:
        points += 1
        user_score.configure(text=points)
        my_api = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
        my_api.raise_for_status()
        mycanvas.configure(background="green")
        window.after(1000, hatdog)
        quiz = my_api.json()["results"][0]
        question = html.unescape(quiz["question"])
        mycanvas.itemconfig(question_api, text= question)
        play(f"true_sound/{random.choice(true_list)}")
    elif quiz["correct_answer"] != answer:
        my_api = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
        my_api.raise_for_status()
        mycanvas.configure(background="red")
        window.after(1000, hatdog)
        quiz = my_api.json()["results"][0]
        question = html.unescape(quiz["question"])
        mycanvas.itemconfig(question_api, text=question)
        play(f"false_sound/{random.choice(false_list)}")

CHECK = ImageTk.PhotoImage(Image.open("myimages/true.png"))
X = ImageTk.PhotoImage(Image.open("myimages/false.png"))
true_button = Button(image=CHECK, highlightthickness=0, activebackground="#AE445A", borderwidth=0, command=true_value)
true_button.place(x=90, y=360)
false_button = Button(image=X, highlightthickness=0, activebackground="#AE445A", borderwidth=0, command=false_value)
false_button.place(y=360, x=310)

window.mainloop()