from ...listener import *
from ...pacman import *

class PacmanViewListener(Listener):
  def on_draw_animal(self, event):
    (animal, view) = event
    if isinstance(animal, Pacman):
      view.draw_pacman(animal)