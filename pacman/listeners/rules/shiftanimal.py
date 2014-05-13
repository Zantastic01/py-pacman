from ...listener import *
from ...directions import *

class ShiftAnimalRuleListener(Listener):
  def on_rules(self, game):
    for monster in game.monsters:
      self.on_rule_animal(monster)

    for pacman in game.pacman:
      self.on_rule_animal(pacman)

  def on_rule_animal(self, animal):
    directions = Directions(animal.field)

    if directions.is_wrong(animal.direction):
      animal.direction = None

    if animal.direction != None:
      animal.shift = animal.shift + animal.SPEED
    else:
      animal.direction = animal.newDirection

    if animal.shift >= 100:
      animal.shift = 0

      animal.field.animals.remove(animal)
      animal.field = animal.field.get(animal.direction)
      animal.field.animals.append(animal)

      directions = Directions(animal.field)
      if not directions.is_wrong(animal.newDirection):
        animal.direction = animal.newDirection
      