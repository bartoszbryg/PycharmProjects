from tkinter import *
import pandas
import random
import math

BACKGROUND_COLOR = "#B1DDC6"

TITLE_FONT = ("Arial", 30, "italic")
WORD_FONT = ("Arial", 60, "bold")
REVERSE_FONT = ("Arial", 20, "bold")


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/polish-english-most-common-words.csv")
    original_data.to_csv("data/words_to_learn.csv", index=False)
    data = pandas.read_csv("data/words_to_learn.csv")


polish_words = data["Polish"].to_list()
english_words = data["English"].to_list()


# data_in_dict = data.to_dict()  # VERY OBJECTIVE METHOD ---> EXTRACTING DATA FROM CSV, MODIFYING IT AND SAVING AGAIN
data_in_dict = data.to_dict(orient="records")  # <----------------- BEST WAY!
# CREATES DICTIONARY IN PARTICULAR WAY - LIST OF ROWS WHERE EVERY ROW IS DICTIONARY - KEY IS NAME OF COLUMN !!!
# VERY USEFUL IF WE CREATE LIST OF PARTICULAR COLUMN AND THEN EXTRACT VALUES - THANKS TO IT WE CAN TAKE ACCURATE ROW

current_polish_word = ""
current_english_word = ""

random_20_words = []

words_forgotten = {
    "Polish": [],
    "English": []
}

word_guessed = 0


# FLASHCARD_GUESSED
def right():
    global word_guessed
    word_guessed += 1
    score_label.config(text=f"{word_guessed}/20")

                                # WRONG !!! - INDEXES IN DATA ARE DIFFERENT FROM INDEXES IN POLISH_WORDS AND ENGLISH_WORDS
    # INCORRECT ------------->  # REMOVING VALUES ONE AT A TIME WILL PRODUCE AN ERROR BECAUSE OF MIXING INDEXES IN LISTS
                                # polish_words = polish_words.remove(current_polish_word)
                                # english_words = english_words.remove(current_english_word)

    # IF WE WANT TO REMOVE PARTICULAR ROWS OR VALUES FROM DATA FRAME
    # WE CAN DO IT BOTH IN DICTIONARIES OR DIRECTLY ON DATA FRAME

    # IF WE WANT TO ADD SOME ROWS OR VALUES TO DATA FRAME WE SHOULD ONLY DO IT BY MODIFYING DICTIONARIES,
    # WE SHOULDN'T DO IT ON DATA FRAMES - THAT DOESN'T WORK !!!
    # ----------------------------------------------------------------------------- #
    # ----------------------------------------------------------------------------- #
    # ----------------------------------------------------------------------------- #
    # ------ 1ST AND 5TH WAY - MODIFYING VALUES BASED ON DICTIONARIES ------ #
    # 1ST WAY- CREATING NEW DICT, EXTRACTING PARTICULAR DATA TO IT AND SAVING NEW DICT
    # 5TH WAY - RECOMMENDED AND BEST!!! - CREATING NEW DICT WITH ALL ORIGINAL VALUES, MODIFYING IT AND SAVING NEW DICT

    # ------- 2ND AND 3RD + 4TH WAY - MODIFYING VALUES BY DROPPING THEM IN ORIGINAL DATA FRAME AT ONCE ----- #
    # 2ND WAY - DROPPING ROWS FROM CURRENT CSV AND SAVING RESULT AGAIN TO CSV (3RD WAY IS SIMILAR -
    # DROPPING VALUES FROM ORIGINAL VARIABLE WITH DATA FRAME AND SAVING RESULT TO THE SAME DATA FRAME)

    # 4TH WAY - LOOPING THROUGH ROWS IN DATA FRAME, SELECTING PARTICULAR ROW AND DROPPING THEM AFTER 'IF' STATEMENT
    # -------------------------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------------------------- #

    # ---- 1ST WAY! - CREATING NEW DICT, DROPPING PARTICULAR ELEMENTS AND ASSIGNING TO EXISTENT CSV ----- #
    # global data # ------------------> the rest of the code should be replaced with data instead of current data
    # current_data = pandas.read_csv("data/words_to_learn.csv")
    # new_dict = {
    #     "Polish": current_data["Polish"].drop(current_data[current_data["Polish"] == current_polish_word].index),
    #     "English": current_data["English"].drop(current_data[current_data["English"] == current_english_word].index)
    # }
    # df = pandas.DataFrame(new_dict)
    # df.to_csv("data/words_to_learn.csv", index=False)
    # -------------------------------------------------------- #
    # -------------------------------------------------------- #
    # -------------------------------------------------------- #

    # ------------------- 2ND WAY! - DROPPING ROWS FROM CURRENT CSV --------------------------- #
    # current_data = pandas.read_csv("data/words_to_learn.csv")
    # print(current_data["Polish"])
    # if current_polish_word in current_data["Polish"].to_list():
    #     current_data = current_data.drop(data[data["Polish"] == current_polish_word].index)
    #
    # current_data.to_csv("data/words_to_learn.csv", index=False)
    # -------------------------------------------------------- #
    # -------------------------------------------------------- #
    # -------------------------------------------------------- #

    # -- 3RD WAY SAME AS 2ND BUT WE MODIFY DATA ON THE ORIGINAL VARIABLE STORING CSV -- #
    # global data
    # print(data["Polish"])
    # if current_polish_word in data["Polish"].to_list():
    #     data = data.drop(data[data["Polish"] == current_polish_word].index)
    #
    # data.to_csv("data/words_to_learn.csv", index=False)
    # -------------------------------------------------------- #
    # -------------------------------------------------------- #
    # -------------------------------------------------------- #

    # ----- 4TH WAY! - LOOPING THROUGH EVERY ROW, EXTRACTING PARTICULAR ROW WITH OUR VALUE AND DROPPING IT ----- #

    # global data
    # print(data["Polish"])
    # -------------------------------------------------------------
    # for index, row in data.iterrows():
    #     if row["Polish"] == current_polish_word:
    #         data = data.drop(index=index)
    # data.to_csv("data/words_to_learn.csv", index=False)
    # ------------------------------------------------------------
    # current_data = pandas.read_csv("data/words_to_learn.csv")        #  <----------------- NOT RECOMMENDED!
    # for index, row in current_data.iterrows():
    #     if row["Polish"] == current_polish_word:
    #         current_data = current_data.drop(index=index)
    #     current_data.to_csv("data/words_to_learn.csv", index=False)

    # ----------------------------------------------------------------------- #
    # ----------------------------------------------------------------------- #
    # ----------------------------------------------------------------------- #

    # - 5TH WAY! - CONVERTING ORIGINAL DATA TO LIST WITH ROWS IN THE BEGINNING,
    # MODIFYING THIS LIST WITH ROWS BY REMOVING PARTICULAR ROW IN DICTIONARY AND SAVING LIST AGAIN TO THE SAME CSV
    # --------- BEST AND RECOMMENDED WAY! ------------ #

    # WE HAVE TO CREATE DICTIONARY WHICH WILL MERGE OUR KEY VALUES IN LIST OF ROWS
    # AND THEN DELETE SIMULTANEOUSLY PARTICULAR VALUES!
    global data_in_dict
    if {"Polish": current_polish_word, "English": current_english_word} in data_in_dict:
        data_in_dict.remove({"Polish": current_polish_word, "English": current_english_word})

    df = pandas.DataFrame(data_in_dict)
    df.to_csv("data/words_to_learn.csv", index=False)

    # ------------------------------------------------------------------------------ #
    # ------------------------------------------------------------------------------ #
    # ------------------------------------------------------------------------------ #
    # ------------------------------------------------------------------------------ #
    # ------------------------------------------------------------------------------ #
    random_20_words.remove(current_polish_word)
    polish_words.remove(current_polish_word)

    card_front_button.grid_remove()
    card_back_button.grid_remove()

    polish_word_button.grid_remove()
    english_word_button.grid_remove()

    create_new_flash_card()


def wrong():
    if current_polish_word not in words_forgotten["Polish"]:
        words_forgotten["Polish"].append(current_polish_word)
        words_forgotten["English"].append(current_english_word)

    df = pandas.DataFrame(words_forgotten)
    df.to_csv("data/words_forgotten.csv", index=False)

    card_front_button.grid_remove()
    card_back_button.grid_remove()

    polish_word_button.grid_remove()
    english_word_button.grid_remove()

    create_new_flash_card()


# ------------------- REVERSE FLASHCARD ----------------------- #
def reverse_to_english():
    card_front_button.grid_remove()
    polish_word_button.grid_remove()

    english_word_button.config(text=current_english_word, bg=card_back_color)
    english_word_button.grid(column=0, row=1, columnspan=2)

    title_lab.config(text="English", fg="white", bg=card_back_color)

    card_back_button.config(image=card_back_img)
    card_back_button.grid(column=0, row=1, columnspan=2)


def reverse_to_polish():
    card_back_button.grid_remove()
    english_word_button.grid_remove()

    polish_word_button.config(text=current_polish_word, bg="white")
    polish_word_button.grid(column=0, row=1, columnspan=2)

    title_lab.config(text="Polish", fg="black", bg="white")

    card_front_button.config(image=card_front_img)
    card_front_button.grid(column=0, row=1, columnspan=2)
    title_lab.config(bg="white")


# --------------- CREATING NEW FLASH CARD ----------------------- #
def create_new_flash_card():
    card_front_button.grid(column=0, row=1, columnspan=2)

    global current_polish_word
    global current_english_word

    if len(random_20_words) == 0:
        global word_guessed
        word_guessed = 0
        if len(polish_words) >= 20:
            for _ in range(20):
                new_card = random.choice(polish_words)
                while new_card in random_20_words:
                    new_card = random.choice(polish_words)

                random_20_words.append(new_card)
        else:
            for _ in range(len(polish_words)):
                new_card = random.choice(polish_words)
                while new_card in random_20_words:
                    new_card = random.choice(polish_words)

                random_20_words.append(new_card)

    current_polish_word = random.choice(random_20_words)

    # You have to extract particular data after 'English' to get string, not Series object - USE ITEM
    current_english_word = data.loc[data["Polish"] == current_polish_word]["English"].item()

    polish_word_button.config(text=current_polish_word, bg="white")
    polish_word_button.grid(column=0, row=1, columnspan=2)

    title_lab.config(text="Polish", bg="white")


# UI Setup

root = Tk()
root.title("Flash Card App")
root.config(width=1000, height=800, padx=50, pady=50, bg=BACKGROUND_COLOR)

# photo_images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# GETTING COLOR FROM CARD BACK
from colorthief import ColorThief

color_thief = ColorThief("images/card_back.png")
# get the dominant color
card_back_color = color_thief.get_color(quality=1)
card_back_color = "#" + '%02x%02x%02x' % card_back_color
print(card_back_color)
# --------------------------------------------- #


# ----------------------------- FIRST WAY ---------------------------------------- #
# canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.create_image(math.floor(canvas.winfo_reqwidth()/2), math.floor(canvas.winfo_reqheight()/2), image=card_front_img)
#
# canvas.create_text(math.floor(canvas.winfo_reqwidth()/2), math.floor(canvas.winfo_reqheight()/2)-150, text="Title", font=TITLE_FONT)
# canvas.create_text(math.floor(canvas.winfo_reqwidth()/2), math.floor(canvas.winfo_reqheight()/2), text="Word", font=WORD_FONT)
# canvas.grid(column=0, row=0, columnspan=2)
#
# reverse_button_1 = Button(root, text="Reverse", width=30, height=2, font=REVERSE_FONT)
# reverse_button_1.grid(column=0, row=0, columnspan=2, sticky=S, pady=50)
#
# reverse_but_2 = Button(root, image=reverse_img, border=0)
# reverse_but_2.grid(column=0, row=0, columnspan=2, sticky=S, pady=55, padx=(400, 0))

# ----------------------------------SECOND WAY -------------------------------------------------#
card_front_button = Button(root, image=card_front_img, font=WORD_FONT, border=0, highlightthickness=0,
                           bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=reverse_to_english)

card_back_button = Button(root, image=card_back_img, font=WORD_FONT, border=0, highlightthickness=0,
                          bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=reverse_to_polish)

title_lab = Label(root, text="Polish", font=TITLE_FONT, bg="white")
title_lab.grid(column=0, row=1, columnspan=2, sticky=N, pady=40)

polish_word_button = Button(root, font=WORD_FONT, bg="white", fg="black", activebackground="white",
                            relief=SUNKEN, border=0, command=reverse_to_english)
# polish_word_button = Label()  polish_word_button can be also label
polish_word_button.grid(column=0, row=1, columnspan=2)

english_word_button = Button(root, font=WORD_FONT, bg=card_back_color, fg="white", activebackground=card_back_color, activeforeground="white",
                             relief=SUNKEN, border=0, command=reverse_to_polish)

# ----------------------------------------------------------------------- #
# ----------------------------------------------------------------------- #
# ----------------------------------------------------------------------- #

score_label = Label(root, text=f"{word_guessed}/20", font=TITLE_FONT, bg=BACKGROUND_COLOR)
score_label.grid(column=0, row=0, columnspan=2, sticky=EW)

right_button = Button(root, image=right_img, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR,
                      command=right)
right_button.grid(column=0, row=2)

wrong_button = Button(root, image=wrong_img, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR,
                      command=wrong)
wrong_button.grid(column=1, row=2)

create_new_flash_card()

root.mainloop()
