class Field:
  def __init__(_self, x, y, fieldType):
    _self.x = x
    _self.y = y
    _self.fieldType = fieldType

  def setNeighbors(_self, neighbors):
    _self.neighbors = neighbors

  def get(_self, direction):
    if direction in _self.neighbors:
      return _self.neighbors[direction]

    return None

  def getTop(_self):
    return _self.get('top')

  def getBottom(_self):
    return _self.get('bottom')

  def getLeft(_self):
    return _self.get('left')

  def getRight(_self):
    return _self.get('right')