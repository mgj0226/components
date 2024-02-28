import pygame

pygame.init()

scrn_w = 800
scrn_h = 450

scrn = pygame.display.set_mode((scrn_w, scrn_h))
pygame.display.set_caption('Health Bar')

class HealthBar():
    def __init__(self, x, y, w, h, max_hp) :
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        #cal ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(250, 200, 300, 40, 100)

run = True
while run:
    scrn.fill("indigo")

    health_bar.hp = 60
    health_bar.draw(scrn)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()