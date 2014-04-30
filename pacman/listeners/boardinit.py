from ..simpleboard import *

class BoardInitListener:
  def on_init(self, game):
    game.board = SimpleBoard().get_board()

    for row in game.board.fields:
      for cell in row:
        game.pacman = game.pacman + cell.pacman
        game.monsters = game.monsters + cell.monsters