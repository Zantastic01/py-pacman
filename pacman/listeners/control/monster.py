import random
from ...listener import *
from ...directions import *

class MonsterControlListener(Listener):
  def on_control(self, game):
    for monster in game.monsters:
      self.on_control_monster(game, monster)

  def on_control_monster(self, game, monster):
    directions = Directions(monster.field)

    if monster.direction == None:
      monster.direction = directions.random()

    if self.change_direction():
      if False == directions.is_wrong(monster.direction):
        nextField = monster.next_field()
        directions = Directions(nextField)
      monster.newDirection = directions.random()

  def change_direction(self):
    return 1 == random.choice(range(1, 5))

