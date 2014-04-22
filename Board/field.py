class Field:
  def __init__(self, x, y, fieldType):
    self.x = x
    self.y = y
    self.fieldType = fieldType

  def set_neighbors(self, neighbors):
    self.neighbors = neighbors

  def get(self, direction):
    if direction in self.neighbors:
      return self.neighbors[direction]

    return None

  def get_top(self):
    return self.get('top')

  def get_bottom(self):
    return self.get('bottom')

  def get_left(self):
    return self.get('left')

  def get_right(self):
    return self.get('right')