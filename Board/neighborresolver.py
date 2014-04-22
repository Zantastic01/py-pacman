from board import *

class NeighborResolver:
  def __init__(_self, board):
    _self.board = board

  def resolve(_self):
    for row in _self.board.fields:
      for cell in row:
        _self.resolveNeighbor(cell)

  def resolveNeighbor(_self, field):
    neighbor = {}
    for char in field.fieldType:
      if char == Board.WALL:
        return
      elif char == Board.TOP:
        neighbor['top'] = _self.board.get(field.x, field.y-1)
      elif char == Board.BOTTOM:
        neighbor['bottom'] = _self.board.get(field.x, field.y+1)
      elif char == Board.LEFT:
        neighbor['left'] = _self.board.get(field.x-1, field.y)
      elif char == Board.RIGHT:
        neighbor['right'] = _self.board.get(field.x+1, field.y)
    field.setNeighbors(neighbor)
