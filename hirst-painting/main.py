# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

import random
from turtle import Turtle, Screen, colormode

color_list = [(205, 161, 86), (58, 88, 128), (142, 91, 40), (136, 26, 50), (219, 208, 109), (133, 173, 200),
              (46, 54, 103), (171, 159, 43), (153, 48, 83), (134, 188, 143), (81, 20, 44), (182, 93, 107), (41, 43, 60),
              (184, 141, 171), (91, 114, 175), (58, 39, 32), (94, 156, 93), (87, 153, 164), (189, 78, 74), (79, 74, 44),
              (62, 117, 114), (47, 74, 76), (217, 177, 189), (47, 76, 75), (169, 206, 169), (180, 187, 210)]


colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
y = -250
tim.setpos(-250, y)


for _ in range(10):
    for _ in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)
    y += 50
    tim.setpos(-250, y)






screen = Screen()
screen.exitonclick()
