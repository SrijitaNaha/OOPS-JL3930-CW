# import and initialize pygame
import pygame

pygame.init()

# set dimensions of the screen
screen = pygame.display.set_mode((600, 600))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# screen fill
screen.fill(white)
pygame.display.update()

# creating a Rectangle class
class Rect():
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

# creating Instances
greenRect = Rect(green, (50, 20, 100, 100))
redRect = Rect(red, (150, 200, 150, 150))
blueRect = Rect(blue, (300, 400, 200, 200))

# accessing methods
greenRect.draw()
blueRect.draw()
redRect.draw()

# Display update to reflect the things on screen
pygame.display.update()

# Main loop to keep the screen open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()