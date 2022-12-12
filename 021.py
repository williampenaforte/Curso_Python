'''william pena forte desafios curso em video python 30/11/2022'''
'''Faça um programa em python que abra e reproduza o audio de uma arquivo mp3'''

import pygame
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
