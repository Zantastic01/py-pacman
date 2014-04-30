class Monster:
  def __init__(self, field, direction = None):
    self.shift = 0
    self.field = field
    self.direction = direction
    print "Utworzylem potwora w " + str(self.field.x) + '_' + str(self.field.y)

  def set_field(self, field):
    self.field = field

