import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
data_dict = data.to_dict()

guessed_states = []
points = 0
game_is_on = True

while len(guessed_states) < 50 and game_is_on:
    if answer_state in states:
        guessed_states.append(answer_state)
        points += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        next_answer = screen.textinput(title=f"{points}/50 States Correct",
                                       prompt="What's another state's name?").title()
        answer_state = next_answer
    elif answer_state == "Exit" or next_answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        e = turtle.Turtle()
        e.hideturtle()
        e.home()
        e.color("Blue")
        e.write(f"You have exited. Final Score: {points}", align="center", font=("Courier", 30, "normal"))
        game_is_on = False
    else:
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        e = turtle.Turtle()
        e.hideturtle()
        e.home()
        e.color("Blue")
        e.write(f"You lose. Final Score: {points}", align="center", font=("Courier", 30, "normal"))
        game_is_on = False


screen.exitonclick()