from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.speed("slowest")
        self.color("white")
        self.setheading(90)
        self.shapesize(1, 5)
        self.goto(position)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
