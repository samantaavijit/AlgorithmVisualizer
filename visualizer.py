import pygame
import sys
import random

pygame.init()
WIDTH = 600
HEIGHT = 512
bar_width = 10
space = 2
delay = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def updateDisplay(array, algorithmName=None, swap1=None, swap2=None, status="Running", sc=screen):
    pygame.time.delay(delay)
    screen.fill((255, 255, 255))
    if status == "Running":
        pygame.display.set_caption("{} Algorithm Visualizer   Status {}....".format(algorithmName, status))
    else:
        pygame.display.set_caption("{} Algorithm Visualizer   Status {}".format(algorithmName, status))

    for i in range(len(array)):
        x = (i * bar_width) + (i * space)
        # + (WIDTH - (len(array) * bar_width + len(array) * space)) / 2
        colour = (80, 0, 255)
        if swap1 == array[i]:
            colour = (0, 255, 0)
        elif swap2 == array[i]:
            colour = (255, 0, 0)
        pygame.draw.rect(sc, colour, (x, WIDTH, bar_width, -array[i]))
    check_events()
    pygame.display.update()


def generate_arr():
    a = random.sample(range(100, HEIGHT), 50)
    return a


if __name__ == '__main__':
    import algorithms

    array = generate_arr()
    # for i in array:
    #     print(i, end=" ")
    updateDisplay(array)
    # algorithms.bubbleSort(array,"Bubble Sort")
    # algorithms.selectionSort(array, "Selection Sort")
    algorithms.insertionSort(array, "Insertion Sort")
    while True:
        check_events()
