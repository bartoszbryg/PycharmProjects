from turtle import Turtle
import pandas


FONT = ("Arial", 8, "normal")
ALIGNMENT = "center"
data = pandas.read_csv("50_states.csv")


class StateManager:
    def __init__(self):
        self.guessed_states = []
        self.all_states = data["state"].tolist()

    def attach_new_state(self, state_name):
        new_state = Turtle()
        new_state_x = int(data[data["state"] == state_name].x)  # MOST IMPORTANT PART OF CSV
        new_state_y = int(data[data["state"] == state_name].y)

        new_state.penup()
        new_state.hideturtle()
        new_state.goto(new_state_x, new_state_y)
        new_state.write(state_name, align=ALIGNMENT, font=FONT)

        self.guessed_states.append(state_name)

    # CREATE CSV WITH NAME OF STATES THE USER DIDN'T GUESS
    def create_csv_file_with_missed_states(self):
        # COMPREHENSION FORM - ONLY ONE LINE !!!!!
        new_data = {"States to learn": [state for state in self.all_states if state not in self.guessed_states]}

        if len(self.guessed_states) != len(self.all_states):
            df = pandas.DataFrame(new_data)
            df.to_csv("missed_states.csv")


# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# NORMAL FORM
# new_data = {
#     "States to learn": []
# }
# for state in self.all_states:
#     if state not in self.guessed_states:
#         new_data["States to learn"].append(state)
