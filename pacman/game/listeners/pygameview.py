from ...view import *

class PygameViewListener:
  def on_view(self, game):
    game.view.draw()