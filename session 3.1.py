import turtle
turtle.speed("fast")
turtle.up()
turtle.goto(-200,100)
turtle.down()

#Draw shape 1( a four-ellipsoidal shape)
turtle.color("red")
turtle.right(112.5)
for i in range(4):
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(50)
    turtle.left(45)


turtle.up()
turtle.goto(100,0.00)
turtle.setheading(0)
turtle.down()

#Draw shape 2( a multil-circle shape)
turtle.color("green")
radius = 20
x = int(input("How many circles do you want? "))
for i in range(1, x + 1):
    turtle.circle(radius*i)


turtle.up()
turtle.goto(200,-300)
turtle.down()

#Daw shape 3
side_number = 4
d = 50
quadrangle_number = int(input("How many stones do you want to have in our shape? "))
turtle.color("red")
turtle.forward(d)
for i in range(quadrangle_number):   
    for i in range(side_number):
        turtle.left(360/side_number)
        turtle.color("blue")
        turtle.forward(d)
        turtle.left(360/side_number)
        turtle.color("red")
        turtle.forward(d)
    side_number += 1



