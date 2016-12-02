import turtle
##draw_square function
def draw_square(length,color):
    turtle.color(color)
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    turtle.left(17)
    turtle.penup()
    turtle.forward(i * 2)
    turtle.pendown()

##draw_star function
def draw_star(x, y,length):
    for i in range(5):
        turtle.left(144)
        turtle.forward(length)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
