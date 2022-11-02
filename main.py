import turtle
import pandas


screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?")
    answer = answer_state.title()
    if answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states_list:
        guessed_states.append(answer)
        answer_t = turtle.Turtle()
        answer_t.hideturtle()
        answer_t.penup()
        state_data = data[data.state == answer]
        answer_t.goto(int(state_data.x), int(state_data.y))
        answer_t.write(state_data.state.item())
        states_list.remove(answer)



screen.mainloop()


