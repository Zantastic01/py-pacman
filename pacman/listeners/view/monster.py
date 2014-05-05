from ...listener import *
from ...monster import *

class MonsterViewListener(Listener):
  def on_draw_animal(self, event):
    (animal, view) = event
    if isinstance(animal, Monster):
      view.draw_monster(animal)