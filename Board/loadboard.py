from board import *
from field import *
from neighborresolver import *

class LoadBoard:
  def __init__(_self, rawBoard):
    _self.board = Board();

    for rawIndex, raw in enumerate(rawBoard):
      tmpRow = []
      for cellIndex, cell in enumerate(raw):
        tmpRow.append(Field(cellIndex, rawIndex, str(cell)))
      _self.board.addRow(tmpRow)
    
    NeighborResolver(_self.board).resolve()

  def getBoard(_self):
    return _self.board