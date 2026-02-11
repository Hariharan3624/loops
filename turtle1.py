import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(600,600)
polygon = turtle.Turtle()
num_sides = 10
side_lenght = 90
angle = 360/num_sides
for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
turtle.done()