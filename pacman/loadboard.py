from board import *
from field import *
from fieldresolver import *
from monsterresolver import  *

class LoadBoard:
  def __init__(self, rawBoard, monsters):
    self.board = Board();

    for rawIndex, raw in enumerate(rawBoard):
      tmpRow = []
      for cellIndex, cell in enumerate(raw):
        tmpRow.append(Field(cellIndex, rawIndex, (0 == cell)))
      self.board.add_row(tmpRow)

    FieldResolver(self.board).resolve()
    MonsterResolver(self.board, monsters).resolve()

  def get_board(self):
    return self.board