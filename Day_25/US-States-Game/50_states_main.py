import turtle
import pandas as pd


states = pd.read_csv("50_states.csv")
guessed_states = []
missed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = states.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another State name?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)

        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("States_to_learn")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=('monaco', 8, 'bold'), align='center')





screen.mainloop()
