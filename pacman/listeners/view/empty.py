from ...listener import *

class EmptyViewListener(Listener):
  def on_draw_element(self, event):
    (x, y, field, view) = event

    view.draw_empty(x, y)
