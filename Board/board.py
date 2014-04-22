class Board:
  WALL = '0'
  TOP = '1'
  BOTTOM = '2'
  LEFT = '3'
  RIGHT = '4'
  fields = []
  def add_row(self, row):
    self.fields.append(row);

  def get(self, x, y):
    maxY = len(self.fields)-1
    if y > maxY:
      return None

    maxX = len(self.fields[y])-1
    if x > maxX:
      return None

    return self.fields[y][x]