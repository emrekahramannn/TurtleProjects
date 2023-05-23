import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board for Kids")

turtle_instance = turtle.Turtle("turtle")

def go_forward():
    turtle_instance.forward(50)

def go_backward():
    turtle_instance.backward(50)

def go_up():
    turtle_instance.left(90)

def go_down():
    turtle_instance.right(90)


drawing_board.listen()
drawing_board.onkey(go_forward, "Up")
drawing_board.onkey(go_backward, "Down")
drawing_board.onkey(go_up, "Right")
drawing_board.onkey(go_down, "Left")

turtle.mainloop()