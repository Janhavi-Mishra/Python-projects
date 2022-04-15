# capstone 2 - turtle crossing game

import time
from turtle import Screen
from turtle_crossing_game import Player, Scoreboard, CarManager

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    if player.ycor() == 280:
        player.refresh()
        scoreboard.level_up()
        car_manager.speed_increase()

    for car in car_manager.all_cars[0:]:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
