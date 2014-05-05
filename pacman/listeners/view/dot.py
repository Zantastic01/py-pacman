from ...listener import *

class DotViewListener(Listener):
  def on_draw_element(self, event):
    (x, y, field, view) = event

    if field.dot:
      view.draw_dot(x, y)