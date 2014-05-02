from board import *
from monster import *
from pacman import *

class FieldResolver:
  def __init__(self, board):
    self.board = board

  def resolve(self):
    for row in self.board.fields:
      for cell in row:
        self.resolve_field(cell)

  def resolve_field(self, field):
    allNeighbors = {
      'left': self.board.get(field.x-1, field.y),
      'right': self.board.get(field.x+1, field.y),
      'top': self.board.get(field.x, field.y-1),
      'bottom': self.board.get(field.x, field.y+1)
    }

    neighbors = {}
    for direction, neighbor in allNeighbors.iteritems():
      if neighbor != None and neighbor.wall == False:
        neighbors[direction] = neighbor

    field.set_neighbors(neighbors)

