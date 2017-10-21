import pygame, sys, random, time


def main():

    check_errors = pygame.init()

    if check_errors[1] > 0:
        print("There was an error in initialization")
        sys.exit(-1)

    else:
        print("Successfully initialized")

    pygame.display.set_caption("Snake game.")
    pygame.display.set_mode((720, 480))
    time.sleep(5)


main()