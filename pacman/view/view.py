import pygame

class View:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("minimal program")
    self.screen = pygame.display.set_mode((800,600))