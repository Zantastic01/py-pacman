class Board:
  WALL = '0'
  TOP = '1'
  BOTTOM = '2'
  LEFT = '3'
  RIGHT = '4'
  fields = []
  def addRow(_self, row):
    _self.fields.append(row);

  def get(_self, x, y):
    maxY = len(_self.fields)-1
    if y > maxY:
      return None

    maxX = len(_self.fields[y])-1
    if x > maxX:
      return None

    return _self.fields[y][x]