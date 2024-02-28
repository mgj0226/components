import pygame
pygame.init()

screen_width = 800
screen_height =450

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Health Bar')

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
    
    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(250, 200, 300, 40, 100)
    
run = True
while run:
    screen.fill("indigo")

    health_bar.hp = 60
    health_bar.draw(screen)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()

pygame.quit()