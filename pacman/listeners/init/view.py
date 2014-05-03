from ...view import *

class ViewInitListener:
  def on_init(self, game):
    game.view = View(game.board);