#Aula 08 - Utilizando Modulo

#Faça um programa em python que abra e reproduza um audio de um arquivo MP3
#importante que o arquivo da musica, esteja na mesma pasta que o arquivo em python
import pygame
pygame.init()
pygame.mixer.music.load("ex01.mp3")
pygame.mixer.music.play()
pygame.event.wait()