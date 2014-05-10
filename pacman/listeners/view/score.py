from pygame import *
from ...listener import *

class ScoreViewListener(Listener):
  def on_draw_info(self, game):
    score = (game.pacman[0].dots*100) + (game.pacman[0].fruits*1000) + (game.pacman[0].monsters*10000)
    game.view.draw_info(10, 15, 'Punkty: ' + str(score));
