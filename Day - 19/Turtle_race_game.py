# concept - more turtle graphics, event listeners, state and multiple instances
from turtle import Turtle, Screen
import random

# TODO: 2) Build a turtle race game
is_race_on = False
screen = Screen()
# setup turtle coordinate system
screen.setup(500, 400)  # (width, height)
# using textinput and num_input method to take user bet
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ").lower()
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []

# using goto method to decide starting line of turtles
i = -120
for name in colours:
    turtle_color = name
    name = Turtle(shape='turtle')
    name.color(turtle_color)
    name.penup()
    name.goto(x=-230, y=i)
    all_turtle.append(name)
    i += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.fillcolor()
            if winning_colour == user_bet:
                print(f'Congratulations, you made the right bet! {winning_colour} turtle wins!')
            else:
                print(f"You've lost! {winning_colour} turtle is the winner!")

        else:
            distance = random.randint(0, 10)
            turtle.forward(distance)

screen.exitonclick()
