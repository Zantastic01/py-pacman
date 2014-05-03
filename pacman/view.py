import pygame

class View:
  WIDTH = 24
  HEIGHT = 24
  screen = None
  board = None
  wallImage = None
  emptyImage = None
  pacmanImage = None
  monsterImage = None
  dotImage = None

  def __init__(self, board):
    self.board = board

    pygame.init()
    pygame.display.set_caption("cat-man by marcin")
    self.screen = pygame.display.set_mode((1024, 768))

    self.wallImage = pygame.image.load('images/wall.png').convert()
    self.emptyImage = pygame.image.load('images/empty.png').convert()
    self.pacmanImage = pygame.image.load('images/pacman.png').convert()
    self.monsterImage = pygame.image.load('images/monster.png').convert()
    self.dotImage = pygame.image.load('images/dot.png').convert()

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

  def draw(self):
    pygame.display.update()   
