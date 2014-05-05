import pygame
from ...monster import *
from ...listener import *

class EndGameRuleListener(Listener):
  def on_rules(self, game):
    pacman = game.pacman[0]

    isAnimalInField = self.check_is_animal(pacman.field)
    if False == isAnimalInField and pacman.shift >= 40:
      nextField = pacman.next_field()
      isAnimalInField = self.check_is_animal(nextField)

    if isAnimalInField:
      self.eventDispatcher.dispatch('end_game', game)

  def check_is_animal(self, field):
    for animal in field.animals:
      if isinstance(animal, Monster):
        return True
    return False

  def on_keypressed(self, event):
    (key, game) = event

    if key == pygame.K_ESCAPE:
      self.eventDispatcher.dispatch('end_game', game)

  def on_end_game(self, game):
    game.ended = True