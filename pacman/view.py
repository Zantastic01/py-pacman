import pygame

class View:
  WIDTH = 24
  HEIGHT = 24

  screen = None
  board = None

  baseImages = {
    'wall' : {
        'path': "images/wall.png"
    },
    'pacman' : {
        'path': "images/pacman.png"
    },
    'monster' : {
        'path': "images/monster.png"
    },
  }

  def __init__(self, board):
    self.board = board

    pygame.init()
    pygame.display.set_caption("cat-man by marcin")

    self.screen = pygame.display.set_mode((800,600))

    for index in self.baseImages.keys():
      image = self.baseImages[index]
      image['image'] = pygame.image.load(image['path'])

  def draw(self):
    maxX = self.board.max_x()
    maxY = self.board.max_y()

    self.screen.fill((0, 0, 0))

    for y in range(0, maxY):
      for x in range(0, maxX):
        field = self.board.get(x, y)

        if field.wall:
          wallRect = self.baseImages['wall']['image'].get_rect().move((x*self.WIDTH, y*self.HEIGHT))
          self.screen.blit(self.baseImages['wall']['image'], wallRect)

        elif len(field.monsters) > 0:
          wallRect = self.baseImages['monster']['image'].get_rect().move((x*self.WIDTH, y*self.HEIGHT))
          self.screen.blit(self.baseImages['monster']['image'], wallRect)
    pygame.display.update()
