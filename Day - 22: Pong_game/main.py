# pong game

# steps - 1) create screen 2) make paddle 1 3) make paddle 2 4) make ball move 5) collision with wall and bounce back
# 6) collision with paddle 7) detect if paddle misses 8) scoreboard

from turtle import Screen
from pong_game import Ball, Paddle, Drawboard, Score
import time

screen = Screen()

# TODO: 1) Screen setup

screen.bgcolor('black')
screen.setup(height=600, width=1000)
screen.title('Pong Game')
screen.tracer(0)

# TODO: 2) Create Paddles

points = int(screen.numinput("Points", "How many points do you want to play for?", default=11, minval=3, maxval=101))

board = Drawboard()
score = Score(points)
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(paddle_r.up, 'Up')  # don't add parenthesis
screen.onkey(paddle_r.down, 'Down')
screen.onkey(paddle_l.up, 'w')
screen.onkey(paddle_l.down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    score.print_score()
    if score.score_l == points or score.score_r == points:
        if score.score_l == score.score_r:
            score.extra_points()
        else:
            score.game_over()
            game_is_on = False
    # TODO: 3) Add the ball
    ball.move()
    # TODO: 4) Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # TODO: 5) Detect collision with paddle and bounce
    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(paddle_r) < 50 or ball.distance(paddle_l) < 50:
            ball.bounce_x()
        # TODO: 6) Refresh if ball misses paddle
        else:
            if ball.xcor() > 400:
                score.r_lose()
                time.sleep(0.3)
                ball.refresh()
            elif ball.xcor() < -400:
                score.l_lose()
                time.sleep(0.3)
                ball.refresh()

screen.exitonclick()
