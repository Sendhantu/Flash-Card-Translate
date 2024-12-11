from operator import indexOf
from tkinter import *
import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Sendhan@2005", database="udemy")

if mydb.is_connected():
    print("Connected to MySQL server")

mycursor = mydb.cursor()
english_words = []
french_words = []
statement = 'SELECT * FROM FLASH_CARD'
mycursor.execute(statement)
data = mycursor.fetchall()
for i in data:
    english_words.append(i[0])
    french_words.append(i[1])

length = len(english_words)
word_pairs = dict(zip(english_words, french_words))

window = Tk()
window.title("Card")
BACKGROUND_COLOR = "#B1DDC6"

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvasbg = Canvas(window, width=850, height=750, bg=BACKGROUND_COLOR)
canvas_image = canvasbg.create_image(425, 300, image=card_front)
texts_item = canvasbg.create_text(425, 200, text="Hello Press the button below to continue", font=("Arial", 30), fill='black')
language_item = canvasbg.create_text(425,150,text='English', font=("Arial", 30), fill='black')
canvasbg.grid(row=0,column=0)

current_word = ""

def right_button_clicked():
    global current_word
    word_right = random.choice(english_words)
    canvasbg.itemconfig(language_item, text='English')
    canvasbg.itemconfig(texts_item, text=word_right)
    current_word = word_right

def wrong_button_clicked():
    global current_word
    word_left = random.choice(english_words)
    canvasbg.itemconfig(language_item, text='English')
    canvasbg.itemconfig(texts_item, text=word_left)
    current_word = word_left

def translate():
    global current_word
    len = indexOf(english_words,current_word)
    french = french_words[len]
    canvasbg.itemconfig(language_item, text="French")
    canvasbg.itemconfig(texts_item, text=french)

#canvasbg.create_image(200, 650, image=right)
#canvasbg.create_image(650, 650, image=wrong)
#right_button = Button(image=right)
#wrong_button = Button(image=wrong)
#right_button.grid(row=1,column=0)
#wrong_button.grid(row=1, column=1)

right_button = Button(image=right,highlightthickness=0,command=right_button_clicked)
wrong_button = Button(image=wrong,highlightthickness=0,command=wrong_button_clicked)
trans_button = Button(text="Translate",highlightthickness=0,command=translate)

canvasbg.create_window(200,650,window=right_button)
canvasbg.create_window(650,650,window=wrong_button)
canvasbg.create_window(425,650,window=trans_button)

#To change the image:
canvasbg.itemconfig(canvas_image, image=card_back)

window.mainloop()