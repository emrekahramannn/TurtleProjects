# import modules
import random
import turtle

# set the screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtles v.2")
screen.screensize(canvwidth=400, canvheight=600)

# initial param.
game_over = False   # check if game is over or not
score = 0           # help to count score
grid_size = 12      # helps to adjust gaps between turtles 

COLORS = ["#DCAE96", "#FFE5B4", "#E6E6FA", "#C8A2C8", "#000080", "#191970", "#FFFFFF", "#FFFDD0"] # hex codes of colors
FONT = ('Times New Roman', 20, 'bold')


# coordinates
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]


#turtle list to hold turtle objects
turtle_list = [] 


# countdown writing turtle
count_down_turtle = turtle.Turtle("turtle")

# score writing turtle
score_turtle = turtle.Turtle("turtle")


def setup_score_turtle():
    """This turtle writes the score"""
    score_turtle.hideturtle()                      # hide the turtle
    score_turtle.pencolor(COLORS[5])               # color of writing
    score_turtle.penup()                           # after finish writing pen up

    # set the position of the writing
    top_height = screen.window_height() / 2        # position (0,0) to (0, y=top)  Total height: 600px  Top: 300px
    y = top_height - (top_height / 10)             # decreasing a bit so text will be visible
    score_turtle.goto(0, y)                        # center the turtle at the top

    # write starting score
    score_turtle.write(arg= 'Score: 0', align="center", font= FONT)    


def make_turtle(x, y):
    """This function makes turtle objects"""
    t = turtle.Turtle("turtle")

    def handle_click(x, y):
        """
        This function detecs if we click on the turtle or not;
        if we click on the turtle then increment the score
        """
        global score
        score += + 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), move=False, align="center", font=FONT)
        # print(x, y)   -> shows the coordinates of 

    t.onclick(handle_click)
    t.penup()
    t.shapesize(1.6, 1.6)
    t.color(random.choice(COLORS))
    t.goto(x * grid_size, y * grid_size)
    t.pendown()
    turtle_list.append(t)


def setup_turtles():
    """This function makes turtle objects in specified coordinates"""
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    """This function hides the turtle objects"""
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)


def countdown(time):
    """This function counts down the time and inform the player every second"""
    global game_over

    top_height = screen.window_height() / 2 # +y max
    y = top_height - (top_height / 10)

    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write(f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)    # show a different turtle every second
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over!", align='center', font=FONT)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()