import pygame

class TickListener:
  FPS = 30
  clock = None
  def on_tick(self, game):
    if self.clock == None:
      self.clock = pygame.time.Clock();

    self.clock.tick(self.FPS)