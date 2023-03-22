# Tocando musica no python
import pygame as pygame

pygame.init()

pygame.mixer.music.load('Death Grips - Klink.mp3')

pygame.mixer.music.play()
input()

pygame.event.wait()
