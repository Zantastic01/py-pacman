from board import *
from field import *
from neighborresolver import *

class LoadBoard:
  def __init__(self, rawBoard):
    self.board = Board();

    for rawIndex, raw in enumerate(rawBoard):
      tmpRow = []
      for cellIndex, cell in enumerate(raw):
        tmpRow.append(Field(cellIndex, rawIndex, str(cell)))
      self.board.add_row(tmpRow)
    
    NeighborResolver(self.board).resolve()

  def get_board(self):
    return self.board