from monster import *

class MonsterResolver:
  def __init__(self, board, monsters):
    self.board = board
    self.monsters = monsters

  def resolve(self):
    for monster in self.monsters:
      field = self.board.get(monster[0], monster[1])
      monster = Monster(field)
      field.add_monster(monster)