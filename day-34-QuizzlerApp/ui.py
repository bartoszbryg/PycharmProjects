import time
from tkinter import *
from math import floor
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

# program_pause_count = "after#0"
# current_count = ""
is_program_paused = False


class QuizInterface(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()

        self.quiz = quiz_brain
        self.title("Quizzler")
        self.config(padx=20, pady=20, background=THEME_COLOR)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.score_lab = Label(self, text="", font=("Arial", 15, "normal"), foreground="white", background=THEME_COLOR)
        self.score_lab.grid(column=1, row=0, pady=20)

        self.result_lab = Label(self, text="", font=("Arial", 15, "bold"), foreground="white", background=THEME_COLOR)
        self.result_lab.grid(column=0, row=1, columnspan=2)

        self.canvas = Canvas(self, background="white", highlightthickness=0, width=300, height=250)
        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()

        self.canvas_text = self.canvas.create_text(floor(canvas_width/2), floor(canvas_height/2),
                                                   text="",
                                                   font=QUESTION_FONT,
                                                   width=280)
        self.canvas.grid(column=0, row=2, columnspan=2)

        self.true_button = Button(self, image=true_img, highlightthickness=0, border=0, activebackground=THEME_COLOR,
                                  command=lambda: self.check_answer("True"))  # command=true_pressed
        self.true_button.grid(column=0, row=3)

        self.false_button = Button(self, image=false_img, highlightthickness=0, border=0, activebackground=THEME_COLOR,
                                   command=lambda: self.check_answer("False"))  # command=false_pressed
        self.false_button.grid(column=1, row=3, pady=20)

        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.result_lab.config(text="")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lab.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            next_question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=next_question_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You've reached the end of the quiz. \n\n"
                                                          f"Final Score: {self.quiz.score}/10")
            self.score_lab.config(text="")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        global is_program_paused
        is_program_paused = False

    def check_answer(self, user_answer):
        # flag is_program_paused solves the bugs regarding after function
        global is_program_paused

        if not is_program_paused:
            is_correct = self.quiz.check_answer(user_answer)
            if is_correct:
                self.result_lab.config(text="You got it right!")
                self.quiz.score += 1
                self.canvas.config(background="green")
            else:
                self.result_lab.config(text="That's wrong!")
                self.canvas.config(background="red")

            self.after(1500, func=self.get_next_question)
            is_program_paused = True



    # def check_answer(self, user_answer):
    #     global program_pause_count, current_count, is_program_paused
    #
    #     if not is_program_paused:
    #         current_count = program_pause_count
    #         is_program_paused = True
    #
    #     print(f"Program_paused_count: {program_pause_count}, current count: {current_count}")
    #     if current_count == program_pause_count:
    #         is_correct = self.quiz.check_answer(user_answer)
    #         if is_correct:
    #             self.result_lab.config(text="You got it right!")
    #             self.quiz.score += 1
    #             self.canvas.config(background="green")
    #         else:
    #             self.result_lab.config(text="That's wrong!")
    #             self.canvas.config(background="red")
    #
    #         program_pause_count = self.after(1500, func=self.get_next_question)


    # def true_pressed(self):
    #     self.quiz.check_answer("True")
    #
    # def false_pressed(self):
    #     self.quiz.check_answer("False")


# ---------------------------------------------------------- #
# ---------------------------------------------------------- #
# ---------------------------------------------------------- #
# ---------------------------------------------------------- #
# ---------------------------------------------------------- #
# ---------------------------------------------------------- #
# ---------------------------------------------------------- #

# 2ND OPTION
# class QuizInterface:
#     def __init__(self):
#         self.window = Tk()
#         self.window.title("Quizzler")
#         self.window.config(padx=20, pady=20, background=THEME_COLOR)
#
#         true_img = PhotoImage(file="images/true.png")
#         false_img = PhotoImage(file="images/false.png")
#
#         self.score_lab = Label(text="Score", font=("Arial", 15, "normal"), foreground="white", background=THEME_COLOR)
#         self.score_lab.grid(column=1, row=0, pady=20)
#
#         self.canvas = Canvas(background="white", width=300, height=250)
#         canvas_width = self.canvas.winfo_reqwidth()
#         canvas_height = self.canvas.winfo_reqheight()
#
#         self.canvas_text = self.canvas.create_text(floor(canvas_width/2), floor(canvas_height/2), text="Some text", font=QUESTION_FONT)
#         self.canvas.grid(column=0, row=1, columnspan=2)
#
#         self.true_button = Button(image=true_img, highlightthickness=0, border=0, activebackground=THEME_COLOR)
#         self.true_button.grid(column=0, row=2)
#
#         self.false_button = Button(image=false_img, highlightthickness=0, border=0, activebackground=THEME_COLOR)
#         self.false_button.grid(column=1, row=2, pady=20)
#
#         self.window.mainloop()

