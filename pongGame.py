# classic ping pong game in python using turtle module

import turtle

# initial setup
win =  turtle.Screen()
win.title("Pong by Justin Ang")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# score
scoreA = 0
scoreB = 0

# adding paddles and ball

# paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)

# paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# ball movement
# move by 2 px
ball.dx = 0.1
ball.dy = -0.1

# score system
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold")) # default score

# functions
def paddleAUp():
    # get y co-ordinate of paddle A
    y = paddleA.ycor()
    y += 20 # add 20 px to y co-ordinate
    # set paddle A's y to new y
    paddleA.sety(y)

def paddleADown():
    # get y co-ordinate of paddle A
    y = paddleA.ycor()
    y -= 20 # remove 20 px to y co-ordinate
    # set paddle A's y to new y
    paddleA.sety(y)

def paddleBUp():
    # get y co-ordinate of paddle B
    y = paddleB.ycor()
    y += 20 # add 20 px to y co-ordinate
    # set paddle B's y to new y
    paddleB.sety(y)

def paddleBDown():
    # get y co-ordinate of paddle B
    y = paddleB.ycor()
    y -= 20 # remove 20 px to y co-ordinate
    # set paddle B's y to new y
    paddleB.sety(y)


# Keyboard bindings
# get user input, when w is pressed, call function paddleAUp to move paddle up
win.listen()
win.onkeypress(paddleAUp, "w")
win.onkeypress(paddleADown, "s")
win.onkeypress(paddleBUp, "Up")
win.onkeypress(paddleBDown, "Down")

# main game loop
while True:
    # update screen
    win.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        # ball hits top border, reverse y direction 'bounce' ball
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        # ball hits bottom border, reverse y direction 'bounce' ball
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        # ball hits right border
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold")) # update printed score

    if ball.xcor() < -390:
        # ball hits left border
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold")) # update printed score

    # when further end of paddle reaches border, reset position of paddle
    if paddleA.ycor() > 355:
        paddleA.goto(-350, 0)

    if paddleA.ycor() < -355:
        paddleA.goto(-350, 0)

    if paddleB.ycor() > 355:
        paddleB.goto(350, 0)

    if paddleB.ycor() < -355:
        paddleB.goto(350, 0)

    # paddle and ball collisions

    # if the ball is between the paddle's height and at its x coordinate, collision occurs
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  
