from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"



def new_word(iterrupt=1):
    global current_card, flipped
    window.after_cancel(flipped)
    current_card = random.choice(to_learn)
    # current_card["French"]
    canvas.itemconfig(flashcard_pic, image=image0)
    canvas.itemconfig(flashcard_title, text="French", fill="black" )
    canvas.itemconfig(flashcard_word, text=current_card["French"], fill="black")
    flipped = window.after(3000, flip_card)

def flip_card():
    global current_card
    # canvas.configure(fg=BACKGROUND_COLOR)
    canvas.itemconfig(flashcard_pic, image=image1)
    canvas.itemconfig(flashcard_title, text="English", fill="white")
    canvas.itemconfig(flashcard_word, text=current_card["English"], fill="white")
    # window.after(3000, new_word)


def remove():
    # global current_card
    to_learn.remove(current_card)
    # print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()



try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_words = pandas.read_csv("data/french_words.csv")
    to_learn = orginal_words.to_dict("records")
else:
    to_learn = words.to_dict("records")
# words=pandas.DataFrame(words)

# print(to_learn)
random_word_nr = random.randint(1, 101)



# print(words)

window = Tk()
window.title("Flashy Flashh")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_card = random.choice(to_learn)
flipped = window.after(3000, flip_card)


yes_image = PhotoImage(file="images/right.png")
no_image = PhotoImage(file="images/wrong.png")
image1=PhotoImage(file="images/card_back.png")


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image0 = PhotoImage(file="images/card_front.png")
flashcard_pic = canvas.create_image(400, 263, image=image0)
flashcard_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
flashcard_word = canvas.create_text(400, 263, text=f'word', fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



yes_button = Button(image=yes_image, bg=BACKGROUND_COLOR, command=remove)
yes_button.grid(column=1, row=1)

no_button = Button(image=no_image, bg=BACKGROUND_COLOR, command=new_word)
no_button.grid(column=0, row=1)


new_word()






window.mainloop()
