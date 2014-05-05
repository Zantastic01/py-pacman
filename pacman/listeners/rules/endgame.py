import pygame
from ...monster import *
from ...listener import *
from ...rules import *

class EndGameRuleListener(Listener):
  def on_rules(self, game):
    pacman = game.pacman[0]

    collisions = Rules().get_collision(pacman, Monster)
    if len(collisions) > 0:
      self.eventDispatcher.dispatch('end_game', game)

  def on_keypressed(self, event):
    (key, game) = event

    if key == pygame.K_ESCAPE:
      self.eventDispatcher.dispatch('end_game', game)

  def on_end_game(self, game):
    game.ended = True