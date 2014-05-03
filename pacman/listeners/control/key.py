import pygame

class KeyControlListener:
  def on_control(self, game):
    eventDispatcher = game.eventDispatcher

    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        eventDispatcher.dispatch('keypressed', [event.key, game])