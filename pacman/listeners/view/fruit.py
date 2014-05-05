from ...listener import *

class FruitViewListener(Listener):
  def on_draw_element(self, event):
    (x, y, field, view) = event

    if field.fruit != None and not field.fruit.eaten:
      view.draw_fruit(x, y, field.fruit.type)