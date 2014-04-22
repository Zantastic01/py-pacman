from board import *

class NeighborResolver:
  def __init__(self, board):
    self.board = board

  def resolve(self):
    for row in self.board.fields:
      for cell in row:
        self.resolve_neighbor(cell)

  def resolve_neighbor(self, field):
    neighbor = {}
    for char in field.fieldType:
      if char == Board.WALL:
        return
      elif char == Board.TOP:
        neighbor['top'] = self.board.get(field.x, field.y-1)
      elif char == Board.BOTTOM:
        neighbor['bottom'] = self.board.get(field.x, field.y+1)
      elif char == Board.LEFT:
        neighbor['left'] = self.board.get(field.x-1, field.y)
      elif char == Board.RIGHT:
        neighbor['right'] = self.board.get(field.x+1, field.y)
    field.set_neighbors(neighbor)
