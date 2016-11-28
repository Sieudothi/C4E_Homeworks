import turtle
wn = turtle.Screen()
turtle.speed("fast")
turtle.penup()
turtle.goto(-300.00,100.00)
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("yellow")

#draw a square
turtle.begin_fill()
for i in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.forward(300)

#draw a triangle
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
for i in range (3):
    turtle.forward(250)
    turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(-200,0.00)
turtle.pendown()

#draw a circle
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(-100,360)
turtle.end_fill()

turtle.penup()
turtle.goto(125,-100)
turtle.pendown()

#draw a mutil-cicle shape
turtle.pencolor("green")
i = 0
for i in range (6):  
    turtle.circle(50)
    turtle.left(60)
##    i = i+ 1 
##    if i>1 and turtle.ycor() == 5.728750807065808e-14:
##        break
    
  
        
    




