import turtle
import random
import time
import os

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("light blue")
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
score = 0

def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

def load_high_score():
    if os.path.isfile("high_score.txt"):
        with open("high_score.txt", "r") as file:
            return int(file.read())
    return 0

high_score = load_high_score()

speed_max = 3
initial_sleep_duration = 0.1
sleep_duration_step = 0.02

def redraw_score():
    score_display.clear()
    score_display.speed(0)
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 260)
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
    score_display.goto(0, -290)
    score_display.color("dark blue")
    score_display.write("Press L to exit", align="center", font=("Courier", 16, "normal"))


# Display the score
score_display = turtle.Turtle()
redraw_score()

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def leave():
    global status
    txt = turtle.textinput("Leave?", "Do you realy want to leave? :() Y/N")
    if txt.lower().strip() == "y":
        status = False

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def check_collision():
    global score
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        return True

    for segment in segments:
        if head.distance(segment) < 20:
            return True

    return False

def generate_food():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)


def update_score():
    global high_score
    if score > high_score:
        high_score = score
        save_high_score(high_score)
        high_score = load_high_score()
    redraw_score()



# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(leave, "L")
screen.onkeypress(leave, "l")



status = True
while status == True:
    screen.update()
    screen.listen()

    time.sleep(initial_sleep_duration - (score//speed_max) * sleep_duration_step)

    if check_collision():
        update_score()
        score = 0
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        leave()

    if head.distance(food) < 20:
        generate_food()
        score += 1
        update_score()

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

