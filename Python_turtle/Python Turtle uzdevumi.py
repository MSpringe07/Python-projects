# Import the turtle module
import turtle

# Create a turtle object
ttl = turtle.Turtle()
ttl.speed(100)
# Set the color and width of the pen
ttl.color("red")
ttl.width(3)

# Loop four times to draw a square
for i in range(4):
    # Move forward by 100 units
    ttl.forward(100)
    # Turn right by 90 degrees
    ttl.right(90)

# Move the turtle to the right of the square
ttl.penup()
ttl.forward(150)
ttl.pendown()

# Change the color to orange
ttl.color("orange")

# Loop eight times to draw an octagon
for i in range(8):
    # Move forward by 50 units
    ttl.forward(50)
    # Turn left by 45 degrees
    ttl.left(45)

# Move the turtle to the right of the square
ttl.penup()
ttl.backward(150)
ttl.left(90)
ttl.forward(150)
ttl.pendown()

# Change the color to blue
ttl.color("blue")

# Loop five times to draw a star
for i in range(5):
    # Move forward by 80 units
    ttl.forward(80)
    # Turn right by 144 degrees
    ttl.right(144)

# Move the turtle to the left of the star
ttl.penup()
ttl.backward(50)
ttl.left(90)
ttl.pendown()

# Change the color to green
ttl.color("green")
ttl.width(2)
# Loop 36 times to draw a Spirograph
for i in range(36):
    # Move forward by 100 units
    ttl.forward(150)
    # Turn left by 170 degrees
    ttl.left(170)

ttl.color("black")
ttl.width(2)

# Move the turtle to the center of the circle
ttl.penup()
ttl.goto(-100, -100)
ttl.pendown()

# Loop 36 times to draw a pattern
for i in range(126):
    # Move forward by 100 units
    ttl.forward(150)
    # Turn right by 170 degrees
    ttl.right(17)
    # Move back by 100 units
    ttl.backward(150)


ttl.penup()
ttl.goto(100, -150)
ttl.pendown()

ttl.color("black")

house = turtle.Turtle()
house.pensize(3)

# Draw the base of the house
house.fillcolor("blue")
house.begin_fill()
for _ in range(2):
    house.forward(200)
    house.right(90)
    house.forward(100)
    house.right(90)
house.end_fill()

# Draw the door
house.color("red")
house.penup()
house.goto(50, -50)
house.pendown()
house.fillcolor("red")
house.begin_fill()
house.right(90)
house.forward(50)
house.right(90)
house.forward(30)
house.right(90)
house.forward(50)
house.end_fill()

# Draw two windows
house.color("white")
for i in range(2):
    house.penup()
    house.goto(100 + i*60, -45)
    house.pendown()
    house.fillcolor("white")
    house.begin_fill()
    for _ in range(4):
        house.forward(30)
        house.right(90)
    house.end_fill()

# Draw the roof of the house
house.color("brown")
house.penup()
house.goto(0,0)
house.pendown()
house.fillcolor("brown")
house.begin_fill()
house.right(60)
house.forward(115)
house.right(60)
house.forward(115)
house.right(150)
house.forward(100)
house.end_fill()

turtle.done()