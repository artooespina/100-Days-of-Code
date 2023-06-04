from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# for x in range(100):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    return tim.color(R,G,B)


# number_of_sides = 3
#
# while number_of_sides <= 9:
#     angle = 360/number_of_sides
#     change_color()
#
#     for x in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#     number_of_sides += 1


# is_on = True
#
# angles = [0, 90, 180, 270]
# tim.speed("fastest")
#
# while is_on:
#     tim.pensize(15)
#     change_color()
#     tim.forward(30)
#     tim.setheading(random.choice(angles))

angle = 0
tim.speed("fastest")

# while angle <= 360:
#     change_color()
#     tim.setheading(angle)
#     tim.circle(100)
#     angle += 5


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
