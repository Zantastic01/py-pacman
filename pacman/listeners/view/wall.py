from ...listener import *

class WallViewListener(Listener):
  def on_draw_element(self, event):
    (x, y, field, view) = event

    if field.wall:
      view.draw_wall(x, y)