import random
from ...game import *

class MonsterCtrlListener:
  SPEED = 20

  def on_control(self, game):
    for monster in game.monsters:
      self.on_control_monster(game, monster)

  def on_control_monster(self, game, monster):
    directions = Directions(monster.field)

    if directions.is_wrong(monster.direction):
      monster.direction = directions.random()

    monster.shift = monster.shift + self.SPEED
    if monster.shift > 100:
      monster.shift = 0

      monster.field.monsters.remove(monster)
      monster.field = monster.field.get(monster.direction)
      monster.field.monsters.append(monster)

      if self.change_direction():
        monster.direction = directions.random()

      print str(monster.field.x) + '_' + str(monster.field.y)

  def change_direction(self):
    return random.choice([True, False])

