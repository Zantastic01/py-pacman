from ...simpleboard import *
from ...listener import *

class BoardInitListener(Listener):
  def on_init(self, game):
    game.board = SimpleBoard().get_board()

    for row in game.board.fields:
      for cell in row:
        if False == cell.wall:
          game.maxDots += 1
        for animal in cell.animals:
          if isinstance(animal, Pacman):
            game.pacman.append(animal)
          elif isinstance(animal, Monster):
            game.monsters.append(animal)