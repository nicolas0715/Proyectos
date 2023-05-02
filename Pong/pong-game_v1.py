import turtle

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=600, height=400)

# Configuración de la paleta izquierda
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Configuración de la paleta derecha
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(250, 0)

# Configuración de la pelota
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# Configuración de los marcadores
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 170)
pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

# Funciones para mover las paletas

# Mover la paleta A hacia arriba
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 130:  # evita que la paleta se mueva fuera de la pantalla hacia arriba
        y += 20
        paddle_a.sety(y)

# Mover la paleta A hacia abajo
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -130:  # evita que la paleta se mueva fuera de la pantalla hacia abajo
        y -= 20
        paddle_a.sety(y)

# Mover la paleta B hacia arriba
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 130:  # evita que la paleta se mueva fuera de la pantalla hacia arriba
        y += 20
        paddle_b.sety(y)

# Mover la paleta B hacia abajo
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -130:  # evita que la paleta se mueva fuera de la pantalla hacia abajo
        y -= 20
        paddle_b.sety(y)

# Configuración de las teclas para mover las paletas
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Bucle principal del juego
while True:
    wn.update()

    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Colisiones con las paredes superior e inferior
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Colisiones con las paletas
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.dx *= -1
    elif (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.dx *= -1

    # Colisiones con las paredes laterales
    if ball.xcor() > 290:
        score_a += 1
        pen.clear()
        pen.write("Jugador A: {} Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -290:
        score_b += 1
        pen.clear()
        pen.write("Jugador A: {} Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
