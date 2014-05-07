import pygame

class SpriteFactory:
  def __init__(self, fileName, width, height):
    self.width = width
    self.height = height
    self.spriteImage = pygame.image.load(fileName).convert_alpha()

  def get_sprites(self):
    return {
      'pacman': self.get_pacman(),
      'monster': {
        1: self.get_monster(1),
        2: self.get_monster(2),
        3: self.get_monster(3)
      },
      'wall': self.get_wall(),
      'dot': self.get_dot(),
      'empty': self.get_empty(),
      'fruits': {
        1: self.get_fruit(1),
        2: self.get_fruit(2),
        3: self.get_fruit(3)
      }
    }

  def get_image(self, x, y):
    image = pygame.Surface([self.width, self.height]).convert_alpha()
    image.blit(self.spriteImage, (0, 0), (x, y, self.width, self.height))
    image.set_colorkey((0, 0, 0))
    return image

  def get_frames(self, y):
    frames = []
    i = 0

    while i < 6:
      frames.append(self.get_image(i*self.width, y))
      i += 1
    return frames

  def get_pacman(self):
    return self.get_frames(0)

  def get_monster(self, monsterType):
    return self.get_frames(self.height + ((monsterType-1)*self.height))

  def get_fruit(self, fruitType):
    return self.get_image((fruitType-1)*self.width, 4*self.height)

  def get_wall(self):
    return self.get_image(0, 5*self.height)

  def get_dot(self):
    return self.get_image(self.width, 5*self.height)

  def get_empty(self):
    return self.get_image(self.width*2, 5*self.height)