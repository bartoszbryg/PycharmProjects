from turtle import Screen
from state_manager import StateManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("US States Guessing Game")
screen.tracer(0)

state_manager = StateManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    user_guess = screen.textinput("Make a guess", prompt="Enter State: ").title()
    screen.update()

    if user_guess == "Exit":
        # state_manager.create_csv_file_with_missed_states()
        # screen.bye()
        break
    # DETECT IF USER ALREADY GUESSED STATE
    if user_guess in state_manager.all_states:
        if user_guess in state_manager.guessed_states:
            scoreboard.already_guessed()
        else:
            state_manager.attach_new_state(user_guess)
            scoreboard.change_score()

    # DETECT IF USER GUESSED WRONG
    if user_guess not in state_manager.all_states:
        scoreboard.bad_guess()

    # for state in state_manager.all_states:
    #     # DETECT IF USER GUESSED RIGHT
    #     if user_guess == state and user_guess not in state_manager.guessed_states:
    #         state_manager.attach_new_state(state)
    #         scoreboard.change_score()

    if scoreboard.score == len(state_manager.all_states):
        scoreboard.win()
        game_is_on = False


state_manager.create_csv_file_with_missed_states()
# screen.exitonclick()






# import turtle
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()