from ...listener import *

class FruitViewListener(Listener):
  def on_draw_element(self, event):
    (x, y, field, view) = event

    if field.fruit != None and not field.fruit.eaten:
      view.draw_fruit(x, y, field.fruit.type)

  def on_draw_info(self, game):
    i = game.maxFruits - game.pacman[0].fruits
    while i > 0:
      game.view.draw_info_fruit(game.view.WIDTH*18 + (game.view.WIDTH*i), 15)
      i -= 1