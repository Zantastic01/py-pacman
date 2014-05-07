class Animal:
  SPEED = 40

  def __init__(self, field, direction = None):
    self.shift = 0
    self.field = field
    self.direction = direction
    self.newDirection = self.direction
    self.frame = 0

  def next_field(self):
    availableNeighbors = self.field.get_available_neighbors()
    if (self.direction in availableNeighbors):
      return self.field.neighbors[self.direction]
    return None