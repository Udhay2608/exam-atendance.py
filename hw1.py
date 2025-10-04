import turtle

t = turtle.Turtle()

length = 150 
width = 100 

for _ in range(2):  
   t.forward(length) 
   t.left(90) 
   t.forward(width)
   t.left(90)

turtle.done()