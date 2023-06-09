from turtle import Turtle, Screen

# Inherit from Turtle class
class PongObject(Turtle):
    def __init__(self, speed, color, position, stretch_wid, stretch_len):
        super().__init__(shape = "square")
        self.speed(speed)
        self.color(color)
        self.shapesize(stretch_wid, stretch_len)
        self.penup()
        self.goto(position)

    # For paddles: move up
    def up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    # For paddles: move up
    def down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)