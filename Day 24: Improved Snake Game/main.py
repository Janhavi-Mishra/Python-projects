from turtle import Screen
from snake_game_improv import Snake, Food, Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)  # to remove animation

# TODO: 1) create a snake body

snake = Snake()  # creating the snake
food = Food()  # create food
scoreboard = Scoreboard()  # TODO: 5) Create a scoreboard

# TODO: 3) Control the snake

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


screen.update()  # to bring the screen back

# TODO: 2) Move the snake

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)  # to slow down the snake

    snake.move()  # moving the snake

    # TODO: 4) Define collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO: 6) Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_game()
        snake.reset_snake()

    # TODO: &) Detect collision with tail
    for segment in snake.turtle_list[1:]:  # slicing lists - list[start: end: increment]
        if snake.head.distance(segment) < 10:
            scoreboard.reset_game()
            snake.reset_snake()

screen.exitonclick()
