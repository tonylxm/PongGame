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


