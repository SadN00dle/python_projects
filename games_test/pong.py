import turtle

win = turtle.Screen()

win.title("pongTest by @Sad_Noodle1")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# paddle a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.color("white")
paddle_a.goto(-350, 0)

# for paddle b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.color("white")
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.penup()
ball.color("white")
ball.goto(0, 0)

# function to move the bawlz
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keys
up_key_a = "w".lower()
down_key_a = "s".lower()

# ball movement
ball.dx = 0.1
ball.dy = 0.1


# moving the paddle
win.listen()
win.onkeypress(paddle_a_up, up_key_a)
win.onkeypress(paddle_a_down, down_key_a)
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while True:
    win.update()

    # moving the bawlz

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dy *= -1

    if ball.ycor() < -390:
        ball.goto(0, 0)
        ball.dy *= -1
