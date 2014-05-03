import pygame
from .. import *

class PacmanControlListener:
  def on_control(self, game):
    pacman = game.pacman[0]
    if pacman.field.dot:
      pacman.field.dot = False
      pacman.dots += 1

  def on_keypressed(self, event):
    (key, game) = event
    pacman = game.pacman[0]

    newDirection = None
    if key == pygame.K_LEFT:
      newDirection = 'left'
    if key == pygame.K_RIGHT:
      newDirection = 'right'
    if key == pygame.K_UP:
      newDirection = 'top'
    if key == pygame.K_DOWN:
      newDirection = 'bottom'

    if newDirection != None:
      print 'Nowy kierunek!: ' + newDirection
      pacman.newDirection = newDirection
