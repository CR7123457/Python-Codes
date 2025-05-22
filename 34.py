import turtle

t = turtle.Turtle()
t.speed(2)
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
  t.forward(100)
  t.left(90)
t.end_fill()

t.penup()
t.goto(150,0)
t.pendown()
t.color("red")
t.circle(50)

turtle.done()
       
   