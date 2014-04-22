from board import *
from ..monster import *
from ..pacman import *

class FieldResolver:
  def __init__(self, board):
    self.board = board

  def resolve(self):
    for row in self.board.fields:
      for cell in row:
        self.resolve_field(cell)

  def resolve_field(self, field):
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
      elif char == Board.MONSTER:
        monster = Monster(field)
        field.add_monster(monster)
      elif char == Board.PACMAN:
        pacman = Pacman(field)
        field.add_pacman(pacman)
    field.set_neighbors(neighbor)
