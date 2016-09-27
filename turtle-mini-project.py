import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.fillcolor("blue")
    brad.pencolor("violet")
    brad.speed(9)

    for i in range (1, 25):
        draw_triangle(brad)
        brad.right(10)

    brad.penup()
    brad.right(-34)
    brad.forward(107)
    brad.pendown()
    
    for i in range(1,37):
        brad.shape("circle")
        brad.circle(33)
        brad.right(10)
        
    draw_line(brad.pos())

    window.exitonclick()

def draw_triangle(my_turtle):
    for i in range (1, 3):
        my_turtle.forward(200)
        my_turtle.right(240)

def draw_line(my_vector):
    tom = turtle.Turtle()
    tom.shape("turtle")
    tom.penup()
    tom.setpos(my_vector)
    tom.pendown()
    tom.pencolor("violet")
    tom.fillcolor("violet")
    tom.right(90)
    tom.forward(300)
    

        
            
draw_art()
