import pygame

from sprite import *

class SpriteFactory:
  def __init__(self, fileName, width, height):
    self.width = width
    self.height = height
    self.spriteImage = pygame.image.load(fileName).convert_alpha()

  def get_sprite(self, name, startX, startY, maxFrames, grayscale = False):
    return Sprite(name, startX, startY, self.width, self.height, self.spriteImage, maxFrames, grayscale)

  def get_sprites(self):
    return [
      self.get_sprite('pacman', 0, 0, 6),
      self.get_sprite('monster1', 0, self.height, 6),
      self.get_sprite('monster2', 0, self.height*2, 6),
      self.get_sprite('monster3', 0, self.height*3, 6),
      self.get_sprite('monster1g', 0, self.height, 6, True),
      self.get_sprite('monster2g', 0, self.height*2, 6, True),
      self.get_sprite('monster3g', 0, self.height*3, 6, True),
      self.get_sprite('wall', 0, self.height*5, 1),
      self.get_sprite('dot', self.width, self.height*5, 1),
      self.get_sprite('empty', self.width*2, self.height*5, 1),
      self.get_sprite('fruit1', 0, self.height*4, 1),
      self.get_sprite('fruit2', self.width, self.height*4, 1),
      self.get_sprite('fruit3', self.width*2, self.height*4, 1)
    ]