import random

class Directions:
  def __init__(self, field):
    self.field = field

  def is_wrong(self, direction):
    directions = self.all()
    return (direction == None) or False == (direction in directions)

  def all(self):
    return self.field.neighbors.keys()

  def random(self):
    return random.choice(self.all())
