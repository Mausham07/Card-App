from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")
current_card= {}



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text="FRENCH", fill="black")
    canvas.itemconfig(canvas_word, text=current_card['French'], fill ="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="ENGLISH", fill="white")
    canvas.itemconfig(canvas_word, text=current_card['English'], fill="white")
    canvas.itemconfig(canvas_image, image=card_front)


window = Tk()
window.title("CARD APP")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400,263,text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img,highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
right_button.grid(row=1, column=1)

next_card()




window.mainloop()