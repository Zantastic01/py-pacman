from ...view import *
from ...listener import *

class ViewInitListener(Listener):
  def on_init(self, game):
    game.view = View(game.board);