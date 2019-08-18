import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.x = 218
        self.y = 368
        self.width = 64
        self.height = 64
        self.jumpCount = 10
        self.falling = True
        self.canJump = True
        self.vel = 4

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))


class Pipe:
    def __init__(self):
        self.x = 550
        self.y = 800
        self.width = 60
        self.height = 400
        self.oldX = 550
        self.randomY1 = 0
        self.randomY2 = random.randint(150, 230)
        self.freeSpace = 800 - ((self.height - self.randomY1) + (self.height - self.randomY2))
        self.canMove = True

    def deathScreen(self):
        font1 = pygame.font.SysFont('comicsans', 80)
        text = font1.render('GAME OVER', 1, (255, 255, 255))
        win.blit(text, (250 - (text.get_width()/2), 340))
        pygame.display.update()
        time.sleep(1.2)


    def draw(self):
        self.freeSpace = 800 - ((self.height - self.randomY1) + (self.height - self.randomY2))
        if self.x <= -60:
            self.x = self.oldX

            rannum = random.randint(1, 2)
            if rannum is 1:
                self.randomY1 = random.randint(180, 250)
                self.randomY2 = 0
            else:
                self.randomY2 = random.randint(180, 250)
                self.randomY1 = 0

        if self.x - bird.width <= bird.x:
            if self.x + bird.width >= bird.x:
                if bird.y >= self.height - self.randomY2:
                    if bird.y <= (self.height - self.randomY2) + self.freeSpace + bird.height:
                        self.canMove = True
                        bird.canJump = True
                        bird.falling = True

        if self.x - bird.width <= bird.x:
            if self.x + bird.width >= bird.x:
                if bird.y <= self.height - self.randomY2 or bird.y >= (self.height - self.randomY2) + self.freeSpace - bird.height:
                    self.canMove = False
                    bird.canJump = False
                    bird.falling = False
                    self.deathScreen()
                    bird.y = 368
                    self.x = self.oldX
                    self.canMove = True
                    bird.canJump = True
                    bird.falling = True

        if self.canMove:
            self.x -= 4


        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - self.height + self.randomY1, self.width, self.height))
        pygame.draw.rect(win, (0, 255, 0), (self.x, 0 - self.randomY2, self.width, self.height))

bird = Player()
pipe = Pipe()
def reDrawWindow():
    win.fill((0,0,0))
    bird.draw()
    pipe.draw()
    pygame.display.update()

run = True
while run:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bird.canJump:
        bird.y -= bird.jumpCount + bird.vel
    if bird.falling:
        bird.y += bird.vel


    if bird.y >= 800 - bird.height - 5:
        bird.falling = False
    if bird.y < 800 - bird.height - 5:
        bird.falling = True

    if bird.y <= 0 + 5:
        bird.canJump = False
    if bird.y > 0 + 5:
        bird.canJump = True

    reDrawWindow()

pygame.quit()