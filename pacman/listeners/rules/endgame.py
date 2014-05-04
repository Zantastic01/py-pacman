import pygame
from ...monster import *

class EndGameRuleListener:
  def on_rules(self, game):
    eventDispatcher = game.eventDispatcher
    pacman = game.pacman[0]

    isAnimalInField = self.check_is_animal(pacman.field)
    if False == isAnimalInField and pacman.shift >= 40:
      nextField = pacman.field.neighbors[pacman.direction]
      isAnimalInField = self.check_is_animal(nextField)

    if isAnimalInField:
      eventDispatcher.dispatch('end_game', game)

  def check_is_animal(self, field):
    for animal in field.animals:
      if isinstance(animal, Monster):
        return True
    return False

  def on_keypressed(self, event):
    (key, game) = event
    eventDispatcher = game.eventDispatcher

    if key == pygame.K_ESCAPE:
      eventDispatcher.dispatch('end_game', game)

  def on_end_game(self, game):
    game.ended = True