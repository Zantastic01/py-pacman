class Animal:
  SPEED = 40

  def __init__(self, field, direction = 'right'):
    self.shift = 0
    self.startField = field
    self.field = field
    self.direction = direction
    self.newDirection = self.direction
    self.frame = 0

  def next_field(self):
    availableNeighbors = self.field.get_available_neighbors()
    if (self.direction in availableNeighbors):
      return self.field.neighbors[self.direction]
    return None

  def setStartField(self):
    self.field.animals.remove(self)
    self.field = self.startField
    self.field.animals.append(self)