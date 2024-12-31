import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
state_list_lower = [state.lower() for state in state_list]

guessed_states = []

correct_state = 0

def display_state(name, x, y):
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(x, y)
    state_turtle.write(name, align="center", font=("Arial", 8, "normal"))

while correct_state != 50:
    answer_state = screen.textinput(title=f"Guess the state, {correct_state} / 50", prompt="Type State name").lower()
    screen.update()

    if answer_state == "exit":
        missing_states = []
        for state in state_list_lower:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in state_list_lower:
        state_list_lower.remove(answer_state)
        guessed_states.append(answer_state)
        correct_state += 1
        print(answer_state)
        state_data = data[data.state.str.lower() == answer_state]
        x, y = int(state_data.x.iloc[0]), int(state_data.y.iloc[0])
        display_state(answer_state.title(), x, y)
    elif answer_state not in state_list_lower and answer_state in guessed_states:
        print("You already guessed that state")
    elif answer_state not in state_list_lower:
        print(f"There is no such a state as {answer_state}")

else:
    print("Congratulations! You guessed all states!")

