class Field():
  def __init__(self, x, y, wall):
    self.x = x
    self.y = y
    self.wall = wall
    self.animals = []
    self.neighbors = {}
    self.dot = True

  def set_neighbors(self, neighbors):
    self.neighbors = neighbors

  def get_available_neighbors(self):
    return self.neighbors.keys()

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

  def add_animal(self, animal):
    self.animals.append(animal)
