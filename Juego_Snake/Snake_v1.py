import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir la clase de la serpiente
class Snake:
    def __init__(self):
        self.size = 2
        self.elements = [[100, 50], [90, 50], [80, 50]]
        self.direction = "right"

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, WHITE, [element[0], element[1], 10, 10])

    def move(self):
        if self.direction == "right":
            head = [self.elements[0][0] + 10, self.elements[0][1]]
        elif self.direction == "left":
            head = [self.elements[0][0] - 10, self.elements[0][1]]
        elif self.direction == "up":
            head = [self.elements[0][0], self.elements[0][1] - 10]
        elif self.direction == "down":
            head = [self.elements[0][0], self.elements[0][1] + 10]
        self.elements.insert(0, head)
        if len(self.elements) > self.size:
            self.elements.pop()

    def change_direction(self, direction):
        if direction == "right" and self.direction != "left":
            self.direction = "right"
        elif direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"

# Definir la clase de la manzana
class Apple:
    def __init__(self):
        self.position = [random.randint(0, 49) * 10, random.randint(0, 49) * 10]

    def draw(self):
        pygame.draw.rect(screen, RED, [self.position[0], self.position[1], 10, 10])

# Inicializar la serpiente y la manzana
snake = Snake()
apple = Apple()

# Definir el reloj
clock = pygame.time.Clock()

# Definir la puntuación
score = 0

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction("right")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("left")
            elif event.key == pygame.K_UP:
                snake.change_direction("up")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("down")

    # Mover la serpiente
    snake.move()

    # Comprobar si la serpiente ha chocado con la pared
    if snake.elements[0][0] < 0 or snake.elements[0][0] > 490 or snake.elements[0][1] < 0 or snake.elements[0][1] > 490:
        pygame.quit()
        quit()
    if snake.elements[0][1] < 0 or snake.elements[0][1] > 490:
        pygame.quit()
        quit()



    # Comprobar si la serpiente ha chocado consigo misma
    for element in snake.elements[1:]:
        if snake.elements[0] == element:
            pygame.quit()
            quit()

    # Comprobar si la serpiente ha comido una manzana
    if snake.elements[0] == apple.position:
        apple = Apple()
        snake.size += 1
        score += 1

    # Dibujar la pantalla
    screen.fill(BLACK)
    snake.draw()
    apple.draw()
    pygame.display.set_caption("Snake - Score: " + str(score))
    pygame.display.update()

    # Establecer la velocidad del juego
    clock.tick(10)

    # Comprobar si se ha alcanzado el objetivo de puntuación
    if score == 20:
        pygame.quit()
        quit()
