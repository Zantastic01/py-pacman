import pygame
from ...listener import *

class TickRuleListener(Listener):
  FPS = 24
  clock = None
  def on_tick(self, game):
    if self.clock == None:
      self.clock = pygame.time.Clock();

    self.clock.tick(self.FPS)