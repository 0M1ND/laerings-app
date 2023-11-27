# Her bruger vi noget som heder Pygame, som er noget andre har lavet. Som skal hjælpe os med at lave lærings appen.
import pygame
pygame.init()

import random

# Importer vores game.py fil, som vi har lavet
from game import *

# Her henter vi skrift typen frem fra mappen
FONT = pygame.font.Font("./Indie.ttf", 24)

BLACK = (0,0,0)
GRAY = (150, 150, 150)

# indsæt sætninger her
sentences = [
    "Jeg(X) spiser(O) aftensmad når jeg(X) kommer(O) hjem.",
    "Jeg(X) synes(O) at han(X) er(O) sød",
    "Hvis han(X) kommer(O) så holder(O) jeg(X) mig væk",
    "Jeg(X) er(O) glad for at du(X) er(O) her",
    "Jeg(X) gik(O) en tur fordi jeg(X) havde(O) lyst.",
    "Forfatteren(X) leger(O) med ordene."
]

# Blander sætningerne
random.shuffle(sentences)

for s in sentences:
    Game.getInstance().add_sentence(s)

class App:
    def __init__(self):
        self.running = True
        self.width = 800
        self.heigth = 300
        self.screen = pygame.display.set_mode((self.width,self.heigth))

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game.getInstance().next_word()

                if event.key == pygame.K_x:
                    Game.getInstance().guess("X")
                    Game.getInstance().next_word()

                if event.key == pygame.K_o:
                    Game.getInstance().guess("O")
                    Game.getInstance().next_word()

                if event.key == pygame.K_BACKSPACE:
                    Game.getInstance().prev_word()

                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw_text(self, text, position, color = (0,0,0)):
        t = FONT.render(text, True, color)
        self.screen.blit(t, position)

    def draw_centered_text(self, text, position, color = (0,0,0)):
        t = FONT.render(text, True, color)
        self.screen.blit(t, (position[0] - t.get_width() / 2, position[1] - t.get_height() / 2))

    def draw(self):
        # Baggrundsfarve
        self.screen.fill((255,255,255))

        self.draw_centered_text("2-Gram", (self.width / 2, 30), (0,0,0))

        # Tegn 1/? i toppen af højre hjørne
        self.draw_text(str(Game.getInstance().current_sentence + 1) + "/" + str(len(Game.getInstance().sentences)), (self.width - 50, 30), GRAY)
        
        # Tegn controls
        self.draw_centered_text("Mellemrum: Næste ord X: Set kryds O: Set bolle Backspace: Fjern og gå tilbage", (self.width / 2, self.heigth - 20), GRAY)

        # Find pygame rect størrelsen på vores sætning
        text = Game.getInstance().get_current_sentence()
        if text != None:
            text = Game.getInstance().sentence_to_string(text)
            text_rect = FONT.render(text, True, (0,0,0)).get_rect()

            # Tegn et ord af gangen
            for i, word in enumerate(Game.getInstance().get_current_sentence()):
                # Find den samlede længde af alle ord indtil nu
                total_width = 0
                for j in range(i):
                    total_width += FONT.render(Game.getInstance().get_current_sentence()[j].word, True, BLACK).get_width() + 10

                # Tegn ordet
                word_rect = FONT.render(word.word, True, BLACK).get_rect()
                self.draw_text(word.word, (self.width / 2 - text_rect.width / 2 + total_width, 180), BLACK) 

                # Hvis ordet er gættet, så tegn det
                if word.guess != None and i != Game.getInstance().current_word:
                    self.draw_text(word.guess, (self.width / 2 - text_rect.width / 2 + total_width + word_rect.width / 2, 210), BLACK)               
                
                # Hvis ordet er det ord vi skal gætte på, så tegn en ^ under ordet
                if i == Game.getInstance().current_word:
                    self.draw_text("^", (self.width / 2 - text_rect.width / 2 + total_width + word_rect.width / 2, 210), BLACK)

        pygame.display.update()

# Her kalder vi init funkstionen. :)
app = App()

while app.running:
    app.tick()
    app.draw()
        
