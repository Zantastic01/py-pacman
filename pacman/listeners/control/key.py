import pygame
from ...listener import *

class KeyControlListener(Listener):
  def on_control(self, game):
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        self.eventDispatcher.dispatch('keypressed', [event.key, game])