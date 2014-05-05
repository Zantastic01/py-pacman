from ...listener import *

class AnimalViewListener(Listener):
  def on_draw(self, event):
    (animal, image, view) = event
    view.draw_animal(animal, image)
