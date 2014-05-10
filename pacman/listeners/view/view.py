from ...listener import *

class ViewListener(Listener):
  def on_view(self, game):
    view = game.view
    board = game.board    
    maxX = board.max_x()
    maxY = board.max_y()

    for y in range(0, maxY):
      for x in range(0, maxX):
        field = board.get(x, y)
        self.eventDispatcher.dispatch('draw_element', [x, y, field, view])

    animals = game.monsters + game.pacman
    for animal in animals:
      self.eventDispatcher.dispatch('draw_animal', [animal, view])

    self.eventDispatcher.dispatch('draw_info', game)

    view.draw();