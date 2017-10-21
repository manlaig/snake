import pygame, sys, random, time


def main():
    check_errors = pygame.init()
    if check_errors[1] > 0:
        print("There was an error in initialization")
        sys.exit(-1)

    else:
        print("Successfully initialized")

main()