import turtle

def main():
    # Create a turtle object
    t = turtle.Turtle()

    # Set the pen color and width
    t.pencolor('black')
    t.width(2)

    # Move the turtle to the starting position
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    # Draw a rectangle
    for i in range(4):
        t.forward(100)
        t.left(90)

    # Move the turtle to a new position
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Draw a circle
    t.circle(50)

    # Move the turtle to a new position
    t.penup()
    t.goto(100, 100)
    t.pendown()

    # Draw a triangle
    for i in range(6):
        t.forward(50)
        t.left(70)

    # Hide the turtle
    t.hideturtle()

    # Exit on click
    turtle.exitonclick()

if __name__ == '__main__':
    main()