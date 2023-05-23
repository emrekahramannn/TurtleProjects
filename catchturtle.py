# import modules
import math         
import random
import turtle


# Inform user 
print("Your score is:\n0")
score = 0
print ("\n" * 2)


# Title: On Screen (Head)
pen_title = turtle.Pen()
pen_title.pencolor("white")
pen_title.hideturtle()
pen_title.penup()
pen_title.setposition(-132,330)
pen_title.write("Catch Me If You Can", font=("Times New Roman", 25, "bold"))


# Hint (Down)
pen_title.pencolor("black")
pen_title.hideturtle()
pen_title.penup()
pen_title.setposition(-135, -340)
pen_title.write("- DON'T TOUCH THE EDGES! -", font=("Times New Roman", 16, "bold italic"))



# Screen
game_board = turtle.Screen()
game_board.bgcolor("#035096") #medium electric blue
game_board.title("Catch the Turtle")


# Set the border
border_turtle = turtle.Turtle()

border_turtle.penup()
border_turtle.speed(15)
border_turtle.hideturtle()
border_turtle.setposition(-300,-300)
border_turtle.pendown()
border_turtle.pensize(4)

for i in range(4):
    border_turtle.color("white")
    border_turtle.forward(620)
    border_turtle.setheading(border_turtle.heading() + 90)



# Create Player
player_turtle = turtle.Turtle()
player_turtle.color("silver")
player_turtle.shape("classic")
player_turtle.penup()
player_turtle.speed(0)


# Goal
objective = turtle.Turtle("turtle")
objective.color("#FFA500") #orange
objective.penup()
objective.speed(0)
objective.setposition(75, -245)


# Initial speed
speed = 1


# Define functions
def rotate_left_angle():
    player_turtle.setheading(player_turtle.heading() + 20)

def rotate_right_angle():
    player_turtle.setheading(player_turtle.heading() - 20)

def increase_speed():
    global speed
    speed += 0.5

def decrease_speed():
    global speed
    speed -= 1
    

#Set keyboard binding
turtle.listen()
turtle.onkey(rotate_right_angle, "Right")
turtle.onkey(rotate_left_angle, "Left")
turtle.onkey(increase_speed, "Up")
turtle.onkey(decrease_speed, "Down")



while True:
    player_turtle.forward(speed)

    # Boundary check
    if player_turtle.xcor() > 306 or player_turtle.xcor() < -306:
        print("GAME OVER")
        quit()

    if player_turtle.ycor() > 306 or player_turtle.ycor() < -306:
        print("Game OVER")
        quit()

    #Collision checking
    d = math.sqrt(math.pow(player_turtle.xcor() - objective.xcor(), 2) + math.pow(player_turtle.ycor() - objective.ycor(), 2))
    if d < 20:
        objective.setposition(random.randint(-300,300), random.randint(-300, 300))
        score = score + 1
        print("Your score is:", score)