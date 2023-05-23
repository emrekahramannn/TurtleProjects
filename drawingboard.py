# import module
import turtle

# set the screen
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board for Kids")


# create the turtle
turtle_instance = turtle.Turtle("turtle")


# define functions for keys

def go_forward():
    turtle_instance.forward(50)

def rotate_right_angle():
    turtle_instance.setheading(turtle_instance.heading() + 10)
    # turtle_instance.right(10)

def rotate_left_angle():
    turtle_instance.setheading(turtle_instance.heading() - 10)
    # turtle_instance.left(10)
    
def clear_screen():
    turtle_instance.clear()

def turtle_go_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()


# connect screen - key
drawing_board.listen()

# assign keys to defined functions
drawing_board.onkey(fun=go_forward, key="space")
drawing_board.onkey(fun=rotate_right_angle, key="Down")
drawing_board.onkey(fun=rotate_left_angle, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_go_home, key="h")

# keep the screen open
turtle.mainloop()