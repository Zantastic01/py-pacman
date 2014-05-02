import pygame

class View:
  WIDTH = 24
  HEIGHT = 24

  screen = None
  board = None

  firstDraw = True

  baseImages = {
    'wall' : {
        'path': "images/wall.png"
    },
    'empty' : {
        'path': "images/empty.png"
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

    self.screen = pygame.display.set_mode((1024,768))

    for index in self.baseImages.keys():
      image = self.baseImages[index]
      image['image'] = pygame.image.load(image['path']).convert()

  def draw(self):
    maxX = self.board.max_x()
    maxY = self.board.max_y()

    BLACK = (0, 0, 0)
    # self.screen.fill(BLACK)

    monsters = []
    for y in range(0, maxY):
      for x in range(0, maxX):
        field = self.board.get(x, y)

        if field.wall == True and self.firstDraw:
          self.draw_wall(x, y)
        elif field.wall == False:
          self.draw_empty(x, y)

        for monster in field.monsters:
          monsters.append(monster)

    for monster in monsters:
      self.draw_monster(monster)

    self.firstDraw = False
    pygame.display.update()

  def draw_wall(self, x, y):
    wallRect = self.baseImages['wall']['image'].get_rect().move((x*self.WIDTH, y*self.HEIGHT))
    self.screen.blit(self.baseImages['wall']['image'], wallRect)

  def draw_empty(self, x, y):
    emptyRect = self.baseImages['empty']['image'].get_rect().move((x*self.WIDTH, y*self.HEIGHT))
    self.screen.blit(self.baseImages['empty']['image'], emptyRect)

  def draw_monster(self, monster):
    x = monster.field.x
    y = monster.field.y
    heightShift = int((self.HEIGHT * monster.shift) / 100);
    widthShift = int((self.WIDTH * monster.shift) / 100);

    if monster.direction == 'top':
      heightShift = -heightShift;
      widthShift = 0;
    elif monster.direction == 'bottom':
      widthShift = 0;
    elif monster.direction == 'left':
      heightShift = 0;
      widthShift = -widthShift;
    elif monster.direction == 'right':
      heightShift = 0;

    wallRectX = (x*self.WIDTH) + widthShift
    wallRectY = (y*self.HEIGHT) + heightShift
    wallRect = self.baseImages['monster']['image'].get_rect().move((wallRectX, wallRectY))
    self.screen.blit(self.baseImages['monster']['image'], wallRect)
