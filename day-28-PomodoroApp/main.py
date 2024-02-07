import time
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    check_mark.config(text="")
    # -------------------------------------------
    # -------------------------------------------
    root.after_cancel(str(timer))   # IMPORTANT !(PARAMETER IS THE VARIABLE WHICH IS RESPONSIBLE FOR PARTICULAR CANCEL)
    # NOTE - 'AFTER' EXECUTES ANOTHER THREAD, AND THEREFORE OTHER PART OF PROGRAM EXECUTES NORMALLY
    # WE NEED TO STOP THIS THREAD USING 'AFTER_CANCEL'
    # -------------------------------------------
    # -------------------------------------------
    canvas.itemconfig(timer_text, text="0:00")
    timer_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    print("start_timer")
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(num_of_seconds):
    minutes = math.floor(num_of_seconds / 60)
    seconds = num_of_seconds % 60

    print(num_of_seconds)

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if num_of_seconds > 0:
        num_of_seconds -= 1
        global timer
        timer = root.after(1000, count_down, num_of_seconds)
        # print(timer)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"

        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Pomodoro")
root.config(padx=200, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)      # VERY, VERY IMPORTANT PART !!!!
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)


timer_label = Label(root, text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(root, text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(root, text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(root, fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


root.mainloop()