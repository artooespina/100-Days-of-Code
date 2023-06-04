from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
xcor = -230
ycor = -70

for item in color:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(item)
    turtle.goto(xcor, ycor)
    ycor += 30
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {user_bet} turtle is the winner!")
            else:
                print(f"You've lost! The {user_bet} turtle is the winner!")

screen.exitonclick()
