# Her bruger vi noget som heder Pygame, som er noget andre har lavet. Som skal hjælpe os med at lave lærings appen.
import pygame
pygame.init()

# Her henter vi skrift typen frem fra mappen
FONT = pygame.font.Font("./Indie.ttf", 32)

class App:
    def __init__(self):
        self.running = True
        self.width = 400
        self.heigth = 500
        self.screen = pygame.display.set_mode((self.width,self.heigth))
        self.button_height = self.width/2 - 30
        
        self.x_button_rect = pygame.Rect(10,self.heigth - self.button_height - 10,self.width/2 - 30,self.button_height)
        self.o_button_rect = pygame.Rect(10 + self.width / 2 + 5,self.heigth - self.button_height - 10,self.width/2 - 30,self.button_height)

    def is_hovering(self, rect):
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos.y > rect.top and mouse_pos.y < rect.bottom:
            if mouse_pos.x > rect.left and mouse_pos.x < rect.right:
                return True
            
        return False

    def tick(self):
        # Kører for hvert "game tick"
        for event in pygame.event.get():
            # Kører for hver event, hver game tick
            if event.type == pygame.QUIT:
                self.running = False

    def draw_text(self, text, position, color = (0,0,0)):
        t = FONT.render(text, True, color)
        self.screen.blit(t, position)

    def draw_centered_text(self, text, center, color = (0,0,0)):
        t = FONT.render(text, True, color)
        rect = t.get_rect(center=center)
        self.screen.blit(t, rect)

    def draw(self):
        # Hvid baggrund
        self.screen.fill((255,255,255))


        if not self.is_hovering(self.x_button_rect):
            pygame.draw.rect(self.screen, (68,201,173), self.x_button_rect)
        pygame.draw.rect(self.screen, (201,84,68), self.o_button_rect)

        pygame.display.update()
        pygame.display.flip()



# Her kalder vi init funkstionen. :)
app = App()

while app.running:
    app.tick()
    app.draw()
        
