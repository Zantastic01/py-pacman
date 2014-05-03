import pygame

class EndGameRuleListener:
  def on_rules(self, event):
    pass

  def on_keypressed(self, event):
    (key, game) = event
    eventDispatcher = game.eventDispatcher

    if key == pygame.K_ESCAPE:
      eventDispatcher.dispatch('end_game', game)

  def on_end_game(self, game):
    game.ended = True