import pygame, sys, random, time


def gameOver():

    font = pygame.font.SysFont('calibri', 100)
    surface = font.render('Game Over!', True, red)
    rect = surface.get_rect()
    rect.midtop = (360, 45)
    screen.blit(surface, rect)
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    sys.exit()


def showScore(isGameOver = False):

    fontSize = 30 if not isGameOver else 56
    font = pygame.font.SysFont('calibri', fontSize)
    surface = font.render('Score: ' + str(score), True, black)
    rect = surface.get_rect()

    xValue = 360 if isGameOver else 65
    yValue = 130 if isGameOver else 30

    rect.midtop = (xValue, yValue)
    screen.blit(surface, rect)


check_errors = pygame.init()
score = 0
fpsController = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(0, 72) * 10, random.randrange(1, 48) * 10]
foodSpawned = True
direction = 'RIGHT'
changeDirectionTo = direction

if check_errors[1] > 0:
    print("There was an error in initialization")
    sys.exit(-1)

else:
    print("Successfully initialized")

pygame.display.set_caption("Snake game.")
screen = pygame.display.set_mode((720, 480))

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)


while True:
    screen.fill(white)
    snake_body.insert(0, list(snake_position))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeDirectionTo = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                changeDirectionTo = 'LEFT'
            elif event.key == pygame.K_UP:
                changeDirectionTo = 'UP'
            elif event.key == pygame.K_DOWN:
                changeDirectionTo = 'DOWN'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if changeDirectionTo == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if changeDirectionTo == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeDirectionTo == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeDirectionTo == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    #changing the direction of the snake

    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10


    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        foodSpawned = False
    else:
        snake_body.pop()

    if not foodSpawned:
        food_position = [random.randrange(0, 72) * 10, random.randrange(1, 48) * 10]
        foodSpawned = True


    for position in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(position[0], position[1], 10, 10))

    pygame.draw.rect(screen, blue, pygame.Rect(food_position[0], food_position[1], 10, 10))

    if snake_position[0] >= 720 or snake_position[0] <= -20 or snake_position[1] >= 490 or snake_position[1] <= -20:
        showScore(True)
        gameOver()

    for snake_blocks in snake_body[1:]:
        if snake_position[0] == snake_blocks[0] and snake_position[1] == snake_blocks[1]:
            showScore(True)
            gameOver()

    showScore()
    pygame.display.flip()

    fpsController.tick(20)
