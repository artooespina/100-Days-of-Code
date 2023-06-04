###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import ensurepip
import colorgram
import turtle as t
import random

t.colormode(255)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")
num_dots_x = 10
num_dots_y = 10

xcor = -250
ycor = -250


for _ in range(num_dots_y):
    turtle.setpos(xcor, ycor)
    for _ in range(num_dots_x):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)

    ycor += 50


screen = t.Screen()
screen.exitonclick()

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# 10 by 10
# dots are 20 in size and spaced by 50
