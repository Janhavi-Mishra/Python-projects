import colorgram as c  # to extract colour from any image
import turtle as t
import random as r

timmy = t.Turtle()
timmy.hideturtle()
screen = t.Screen()


# TODO: 1) create colour list by extracting colours from image

def extract_colours(image, no_of_colours):  # function to extract colour from image and print in a list
    colours_1 = c.extract(image, no_of_colours)
    colour_list = []

    for number in range(no_of_colours):
        colour_item = (colours_1[number].rgb.r, colours_1[number].rgb.g, colours_1[number].rgb.b)
        colour_list.append(colour_item)

    return colour_list


# TODO: 2) Draw the dots using colour list created - 10 x 10 dots - dia = 20 - space = 50

colours = extract_colours('image.jpg', 30)

screen.colormode(255)
set_x = -200.00
set_y = -200.00

for y in range(10):
    timmy.penup()
    timmy.goto(set_x, set_y + (y * 50))  # to set position of turtle
    for x in range(10):
        timmy.dot(20, r.choice(colours))
        timmy.penup()
        timmy.fd(50)

screen.exitonclick()
