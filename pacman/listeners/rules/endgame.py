import pygame
from ...monster import *
from ...listener import *
from ...rules import *

class EndGameRuleListener(Listener):
  def on_rules(self, game):
    pacman = game.pacman[0]

    collisions = Rules().get_collision(pacman, Monster)
    if len(collisions) > 0:
      self.eventDispatcher.dispatch('pacman_collision', game)

    if game.maxDots == pacman.dots:
      self.eventDispatcher.dispatch('end_game', game)
      self.eventDispatcher.dispatch('pacman_win', game)

  def on_pacman_collision(self, game):
    self.eventDispatcher.dispatch('pacman_lost_life', game)

    game.lifes -= 1
    if game.lifes <= 0:
      self.eventDispatcher.dispatch('end_game', game)
      self.eventDispatcher.dispatch('pacman_lost', game)

    game.pacman[0].setStartField()
    for monster in game.monsters:
      monster.setStartField()

  def on_keypressed(self, event):
    (key, game) = event

    if key == pygame.K_ESCAPE:
      self.eventDispatcher.dispatch('end_game', game)

  def on_end_game(self, game):
    game.ended = True