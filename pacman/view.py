import pygame
from spritefactory import *

class View:
  WIDTH = 36
  HEIGHT = 36
  screen = None
  board = None
  sprites = []

  def __init__(self, board):
    self.board = board

    pygame.init()
    pygame.display.set_caption("cat-man by marcin")
    self.screen = pygame.display.set_mode((1024, 768))
    self.sprites = SpriteFactory('images/sprites.png', self.WIDTH, self.HEIGHT).get_sprites()

  def search_sprite(self, name):
    for sprite in self.sprites:
      if sprite.name == name:
        return sprite
    return None

  def draw_animal(self, animal, image):
    x = animal.field.x
    y = animal.field.y
    heightShift = int((self.HEIGHT * animal.shift) / 100);
    widthShift = int((self.WIDTH * animal.shift) / 100);

    if animal.direction == 'top':
      heightShift = -heightShift;
      widthShift = 0;
    elif animal.direction == 'bottom':
      widthShift = 0;
    elif animal.direction == 'left':
      heightShift = 0;
      widthShift = -widthShift;
    elif animal.direction == 'right':
      heightShift = 0;

    wallRectX = (x*self.WIDTH) + widthShift
    wallRectY = (y*self.HEIGHT) + heightShift

    wallRect = image.get_rect().move((wallRectX, wallRectY))
    self.screen.blit(image, wallRect)

  def draw_pacman(self, pacman):
    rotate = {
      'top': 90,
      'bottom': -90,
      'left': -180,
      'right': 0
    }

    pacmanImage = self.search_sprite('pacman').next_frame(pacman)
    if pacman.direction in rotate.keys():
      pacmanImage = pygame.transform.rotate(pacmanImage, rotate[pacman.direction])

    self.draw_animal(pacman, pacmanImage)


  def draw_monster(self, monster):
    image = self.search_sprite('monster1').next_frame(monster)
    if False == monster.active:
      image = self.search_sprite('monster1').next_frame(monster)

    self.draw_animal(monster, image)

  def draw_fruit(self, x, y, fruitType):
    self.draw_image(x, y, self.search_sprite('fruit' + str(fruitType)).get_frame(0))

  def draw_empty(self, x, y):
    self.draw_image(x, y, self.search_sprite('empty').get_frame(0))

  def draw_wall(self, x, y):
    self.draw_image(x, y, self.search_sprite('wall').get_frame(0))

  def draw_dot(self, x, y):
    self.draw_image(x, y, self.search_sprite('dot').get_frame(0))

  def draw_image(self, x, y, image):
    imageRect = image.get_rect().move((x*self.WIDTH, y*self.HEIGHT))
    self.screen.blit(image, imageRect)

  def draw(self):
    pygame.display.update()
    self.screen.fill((0, 0, 0))
