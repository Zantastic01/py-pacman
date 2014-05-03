import random
from .. import *

class MonsterControlListener:
  def on_control(self, game):
    for monster in game.monsters:
      self.on_control_monster(game, monster)

  def on_control_monster(self, game, monster):
    directions = Directions(monster.field)

    if monster.direction == None:
      monster.direction = directions.random()

    if self.change_direction():
      monster.newDirection = directions.random()

  def change_direction(self):
    return random.choice([True, False, True])

