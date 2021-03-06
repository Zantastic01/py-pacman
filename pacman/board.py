class Board:
  fields = []

  def add_row(self, row):
    self.fields.append(row)

  def max_y(self):
    return len(self.fields)

  def max_x(self):
    return len(self.fields[0])

  def get(self, x, y):
    maxY = len(self.fields)-1
    if y > maxY:
      return None

    maxX = len(self.fields[y])-1
    if x > maxX:
      return None

    return self.fields[y][x]
