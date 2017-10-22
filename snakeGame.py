import pygame, sys, random, time


check_errors = pygame.init()

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

fpsController = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

food_position = [random.randrange(0, 72) * 10, random.randrange(0, 48) * 10]
foodSpawned = True

direction = 'RIGHT'
changeDirectionTo = direction

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeDirectionTo = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeDirectionTo = 'LEFT'
            if event.key == pygame.K_UP:
                changeDirectionTo = 'UP'
            if event.key == pygame.K_DOWN:
                changeDirectionTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()



def gameOver():
    font = pygame.font.SysFont('monaco', 100)
    surface = font.render('Game Over!', True, red)
    rect = surface.get_rect()
    rect.midtop = (360, 45)
    screen.blit(surface, rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()