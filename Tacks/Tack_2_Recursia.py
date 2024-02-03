import turtle

def pythagorean_tree(t, order, size, angle):
    if order == 0:
        return
    else:
        t.forward(size)
        t.left(angle)
        pythagorean_tree(t, order - 1, size * 0.7, angle)
        t.right(2 * angle)
        pythagorean_tree(t, order - 1, size * 0.7, angle)
        t.left(angle)
        t.backward(size)

def draw_pythagorean_tree(order, size=100, angle=45):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(0, -size / 2)
   
    t.left(90)
    t.pendown()

    pythagorean_tree(t, order, size, angle)

    window.mainloop()

# Будуємо дерево піфагора
draw_pythagorean_tree(7, size=200, angle=60)