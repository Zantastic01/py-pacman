from .. import *

class ViewListener:
  def on_view(self, game):
    eventDispatcher = game.eventDispatcher
    view = game.view
    board = game.board    
    maxX = board.max_x()
    maxY = board.max_y()

    for y in range(0, maxY):
      for x in range(0, maxX):
        field = board.get(x, y)

        if field.wall == True:
          eventDispatcher.dispatch('draw_wall', [x, y, view])
        elif field.wall == False:
          if field.dot == True:
            eventDispatcher.dispatch('draw_dot', [x, y, view])
          else:
            eventDispatcher.dispatch('draw_empty', [x, y, view])

    for monster in game.monsters:
      eventDispatcher.dispatch('draw_animal', [monster, view.monsterImage, view])

    for pacman in game.pacman:
      eventDispatcher.dispatch('draw_animal', [pacman, view.pacmanImage, view])

    view.draw();