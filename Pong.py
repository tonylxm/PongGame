# AUTHOR: Tony Lim
# DATE STARTED:22/04/2023
# DATE LAST EDITED:22/04/2023

# Pong Game
from PongObject import PongObject, Screen

# Create window
wn = Screen()
wn.title("PONG by Tony Lim")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)    # Stops window from updating -> manually update -> faster game

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
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
