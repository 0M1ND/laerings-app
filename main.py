# Her bruger vi noget som heder Pygame, som er noget andre har lavet. Som skal hjælpe os med at lave lærings appen.
import pygame
pygame.init()

# Importer vores game.py fil, som vi har lavet
import game

# Her henter vi skrift typen frem fra mappen
FONT = pygame.font.Font("./Indie.ttf", 32)
LARGE_FONT = pygame.font.Font("./Indie.ttf", 58)

game = game.Game()
game.add_sentence("Jeg(O) spiser(X) aftensmad når jeg(O) kommer(X) hjem.")

class App:
    def __init__(self):
        self.running = True
        self.width = 400
        self.heigth = 500
        self.screen = pygame.display.set_mode((self.width,self.heigth))
        self.button_height = self.width/2 - 30
        
        self.selected = None;
        self.O_button_rect = pygame.Rect(10,self.heigth - self.button_height - 10,self.width/2 - 30,self.button_height)
        self.X_button_rect = pygame.Rect(10 + self.width / 2 + 5,self.heigth - self.button_height - 10,self.width/2 - 30,self.button_height)

    def is_hovering(self, rect):
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[1] > rect.top and mouse_pos[1] < rect.bottom:
            if mouse_pos[0] > rect.left and mouse_pos[0] < rect.right:
                return True
            
        return False

    def tick(self):
        # Kører for hvert "game tick"
        for event in pygame.event.get():
            # Kører for hver event, hver game tick
            if event.type == pygame.QUIT:
                self.running = False

            # Hvis vi klikker på musen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_hovering(self.O_button_rect):
                    self.selected = "O"
                elif self.is_hovering(self.X_button_rect):
                    self.selected = "X"
                print(self.selected)

    def draw_text(self, text, position, color = (0,0,0)):
        t = FONT.render(text, True, color)
        self.screen.blit(t, position)

    # Taget fra: https://stackoverflow.com/questions/49432109/how-to-wrap-text-in-pygame-using-pygame-font-font
    def renderTextCenteredAt(self, text, font, colour, x, y, allowed_width):
        # first, split the text into words
        words = text.split()

        # now, construct lines out of these words
        lines = []
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break

            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)

        # now we've split our text into lines that fit into the width, actually
        # render them

        # we'll render each line below the last, so we need to keep track of
        # the culmative height of the lines we've rendered so far
        y_offset = 0
        for line in lines:
            fw, fh = font.size(line)

            # (tx, ty) is the top-left of the font surface
            tx = x - fw / 2
            ty = y + y_offset

            font_surface = font.render(line, True, colour)
            self.screen.blit(font_surface, (tx, ty))

            y_offset += fh

    def darken_color(self, color, amount):
        r = color[0] - amount
        g = color[1] - amount
        b = color[2] - amount

        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0
            
        return (r,g,b)

    def draw(self):
        # Hvid baggrund
        self.screen.fill((255,255,255))
        

        
        pygame.draw.rect(self.screen, (68,201,173), self.O_button_rect, 10 if self.selected == "O" else 0)
        self.renderTextCenteredAt("O", LARGE_FONT, (0,0,0), self.O_button_rect.centerx, self.O_button_rect.centery - 40, self.O_button_rect.width)
        pygame.draw.rect(self.screen, (201,84,68), self.X_button_rect, 10 if self.selected == "X" else 0)
        self.renderTextCenteredAt("X", LARGE_FONT, (0,0,0), self.X_button_rect.centerx, self.X_button_rect.centery - 40, self.X_button_rect.width)


        self.renderTextCenteredAt(game.getInstance().sentence_to_string(game.getInstance().sentences[0]), FONT, (0,0,0), self.width/2, 100, self.width - 20)

        pygame.display.update()
        pygame.display.flip()



# Her kalder vi init funkstionen. :)
app = App()

while app.running:
    app.tick()
    app.draw()
        
