import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"


screen.addshape(image)
turtle.shape(image)


def write_on_map(guess, coordinates):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(coordinates)
    state.write(guess, align="center", font=("Arial", 8, "normal"))


def get_coordinates(guess):
    guess_state = data[data.state == guess]
    x_cor = int(guess_state.x)
    y_cor = int(guess_state.y)
    return x_cor, y_cor


data = pandas.read_csv("50_states.csv")
data_state = data.state
correct_guesses = []
num_correct = 0
should_continue = True

guess = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while should_continue:
    if guess in correct_guesses:
        pass
    else:
        for state in data_state:
            if state == guess:
                coordinates = get_coordinates(guess)
                write_on_map(guess, coordinates)

                correct_guesses.append(guess)
                num_correct += 1
            else:
                pass

    guess = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state's name?").title()

# print(data.data["state"] == answer_state)
# states = data.state.to_list()
#
#
# print(data["state"] == answer_state)




screen.exitonclick()