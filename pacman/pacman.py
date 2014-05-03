class Pacman:
  SPEED = 40

  def __init__(self, field, direction = 'bottom'):
    self.shift = 0
    self.field = field
    self.direction = direction
    self.newDirection = direction
    self.dots = 0
    print "Utworzylem pacmana w " + str(self.field.x) + '_' + str(self.field.y)