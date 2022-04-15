from turtle import Turtle

FONT = ('Courier', 20, 'normal')
UP = 90
DOWN = 270
DISTANCE = 20


class Drawboard(Turtle):
    """Setup of the game board"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.draw_board()

    def draw_board(self):
        # to draw circle in center
        self.penup()
        self.goto(0, -100)
        self.pendown()
        self.circle(100)
        # to draw center line
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.goto(0, 300)
        # to draw side lines
        self.penup()
        self.goto(380, 300)
        self.pendown()
        self.goto(380, -300)
        self.penup()
        self.goto(-380, 300)
        self.pendown()
        self.goto(-380, -300)


class Score(Turtle):
    """Score tracking and printing"""

    def __init__(self, points):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.points = points
        self.score_l = 0
        self.score_r = 0

    def print_score(self):
        self.clear()
        self.goto(250, 250)
        self.write(f'Player A: {self.score_r}', align='center', font=FONT)
        self.goto(-250, 250)
        self.write(f'Player B: {self.score_l}', align='center', font=FONT)

    def extra_points(self):
        self.points += 1

    def l_lose(self):
        self.score_r += 1

    def r_lose(self):
        self.score_l += 1

    def game_over(self):
        if self.score_r == self.points:
            self.goto(250, 150)
            self.write('|GAME OVER|\nPlayer A wins!', align='center', font=FONT)
        elif self.score_l == self.points:
            self.goto(-230, 150)
            self.write('|GAME OVER|\nPlayer B wins!', align='center', font=FONT)


class Ball(Turtle):
    """Functions related to movement of ball"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # increase seed after every hit

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()  # reverse direction of ball to change turn
        self.move_speed = 0.1  # reset speed


class Paddle(Turtle):
    """Functions related to movement of paddle"""

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1, 5)
        self.color('white')
        self.goto(position)
        self.setheading(90)

    def up(self):
        if self.ycor() < 250:
            self.forward(DISTANCE)
        else:
            pass

    def down(self):
        if self.ycor() > -230:
            self.backward(DISTANCE)
        else:
            pass
