import pandas
import turtle

img = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(img)
turtle.shape(img)




data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_list = []
        for state in state_list:
            if state not in guessed_states:
                missing_list.append(state)
        new_data = pandas.DataFrame(missing_list)
        new_data.to_csv("new_data.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.pu()
        tim.hideturtle()
        state_write = data[data.state == answer_state]
        x = int(state_write.x)
        y = int(state_write.y)
        tim.goto(x, y)
        tim.write(state_write.state.item())




