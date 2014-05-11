from ...listener import *

class LifeViewListener(Listener):
  def on_draw_info(self, game):
    i = game.lifes
    while i > 0:
      game.view.draw_life(game.view.WIDTH*23 + (game.view.WIDTH*i), 15)
      i -= 1