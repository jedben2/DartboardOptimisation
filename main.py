# Details of the maths is in README.md

import pygame
import numpy as np
from itertools import product

pygame.init()

win = pygame.display.set_mode((800, 800))
white = (255, 255, 255)
board = pygame.image.load("dartboardcolourscore-transformed.png")


def f(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (np.sqrt(2 * np.pi) * sigma)


def score(P):
    col = win.get_at(P)
    if col[1] != 0:
        return 0
    else:
        return col[0] // 4


def E(xs, ys):
    total = 0
    for x, y in zip(xs, ys):
        print(score((int(x), int(y))))
        total += score((int(x), int(y))) / len(xs)
    return total


mu = np.array([0, 0])
sigma = 1
xs, ys = [], []

running = True
mousedown = False
r = 0
while running:
    win.fill(white)
    win.blit(board, (-6, -6))
    if mousedown:
        r = np.linalg.norm(np.array(pygame.mouse.get_pos()) - mu)
        pygame.draw.circle(win, center=mu, radius=r, color=white, width=1)
        pygame.draw.line(win, color=white, start_pos=mu, end_pos=pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mousedown:
                sigma = r / 3
                xs = np.random.normal(mu[0], sigma, 1000)
                ys = np.random.normal(mu[1], sigma, 1000)
                print(E(xs, ys))
            else:
                mu = np.array(pygame.mouse.get_pos())
            mousedown = not mousedown

    for x, y in zip(xs, ys):
        pygame.draw.circle(win, center=[x, y], color=white, radius=1)
    pygame.display.flip()
