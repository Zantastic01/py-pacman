from board import *
from field import *
from fieldresolver import *
from fruitresolver import *
from monsterresolver import  *
from pacmanresolver import *

class LoadBoard:
  def __init__(self, rawBoard, monsters, pacman, fruits):
    self.board = Board();

    for rawIndex, raw in enumerate(rawBoard):
      tmpRow = []
      for cellIndex, cell in enumerate(raw):
        tmpRow.append(Field(cellIndex, rawIndex, (0 == cell)))
      self.board.add_row(tmpRow)

    FieldResolver(self.board).resolve()
    MonsterResolver(self.board, monsters).resolve()
    PacmanResolver(self.board, pacman).resolve()
    FruitResolver(self.board, fruits).resolve()

  def get_board(self):
    return self.board