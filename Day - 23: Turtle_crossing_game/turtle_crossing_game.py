from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

MOVE_DISTANCE = 10
START_POSITION = (0, -280)
FINISH_LINE_Y = 280

FONT = ('Courier', 24, 'normal')


class CarManager(Turtle):
    """Control cars and their movement"""
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 3:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_increase(self):
        self.speed += MOVE_INCREMENT


class Scoreboard(Turtle):
    """Keep track of score and write on screen"""
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write_score()

    def level_up(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Level {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('|GAME OVER|', align='center', font=FONT)


class Player(Turtle):
    """Control movement of player turtle"""
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.refresh()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(START_POSITION)
