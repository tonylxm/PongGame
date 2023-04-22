# AUTHOR: Tony Lim
# DATE STARTED:22/04/2023
# DATE LAST EDITED:22/04/2023

# Pong Game
import turtle
from PongObject import PongObject, Screen

# Create window
wn = Screen()
wn.title("PONG by Tony Lim")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)    # Stops window from updating -> manually update -> faster game

# Score
score_a = 0
score_b = 0

# Create paddles
paddle_a = PongObject(0, "white", (-350, 0), 5, 1)
paddle_b = PongObject(0, "white", (350, 0), 5, 1)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a.up, "w")
wn.onkeypress(paddle_a.down, "s")
wn.onkeypress(paddle_b.up, "Up")
wn.onkeypress(paddle_b.down, "Down")

# Create ball
ball = PongObject(0, "white", (0, 0), 1, 1)
ball.dx = 0.1
ball.dy = 0.1

# Create scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Main game loop
while True:
    wn.update() # Manually update window

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    
    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1