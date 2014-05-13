from ...listener import *
import time

class MessagesViewListener(Listener):
  def on_pacman_lost_life(self, game):
    game.view.draw_message('Monster ate you!')
    time.sleep(2)

  def on_pacman_win(self, game):
    game.view.draw_message('Congratulations! You won!')
    time.sleep(5)

  def on_pacman_lost(self, game):
    game.view.draw_message('Sorry! You lose!')
    time.sleep(5)

  def on_init(self, game):
    i = 3
    while i>0:
      game.view.draw_message('Start game in.. ' + str(i))
      time.sleep(1)
      i -= 1
