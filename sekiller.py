import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("pink")
turtle_screen.title("turtle python")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")

def sekiller(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

sekiller(150)
sekiller(130)
sekiller(110)
sekiller(90)
sekiller(70)
sekiller(50)
sekiller(30)
sekiller(10)



turtle.done()