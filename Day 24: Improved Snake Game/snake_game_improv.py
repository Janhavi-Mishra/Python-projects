from turtle import Turtle
import random

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
STARTING_POSITION = [(20, 0), (0, 0), (-20, 0)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Control of the snake"""

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]
        self.move_speed = 0.3

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.fillcolor('white')
        new_turtle.setpos(position)
        self.turtle_list.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())
        self.move_speed *= 0.9

    def move(self):
        for seg in range(len(self.turtle_list) - 1, 0, -1):  # start,stop,step
            new_x = self.turtle_list[seg - 1].xcor()  # move one segment to the next ones position
            new_y = self.turtle_list[seg - 1].ycor()
            self.turtle_list[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.turtle_list:
            seg.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]
        self.move_speed = 0.3


# TODO: Day- 21 - Class Inheritance and slicing + Snake game complete
# class inheritance is taking methods from existing classes n add it to a new class

class Scoreboard(Turtle):
    """Score record"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 290)
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"High Score: {self.high_score} Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.track_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as file:
            file.write(f'{self.high_score}')


# def game_over(self):
#    self.goto(0, 0)
#   self.write("| GAME OVER |", align=ALIGNMENT, font=FONT)


class Food(Turtle):  # to inherit from Turtle, add it after name of class food
    """Control movement of food"""

    def __init__(self):
        super().__init__()  # create an init for turtle in food
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # to dec size from 20*20 to 10*10
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        self.goto(random_x, random_y)
