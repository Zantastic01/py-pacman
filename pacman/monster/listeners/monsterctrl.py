from random import randint

class MonsterCtrlListener:
  SPEED = 20

  def on_control(self, game):
    for monster in game.monsters:
      self.on_control_monster(game, monster)

  def on_control_monster(self, game, monster):
    monster.shift = monster.shift + self.SPEED

    if monster.shift > 100:
      monster.shift = 0
      monster.field = monster.field.get(monster.direction)

    if (self.change_direction()):
      monster.direction = self.random_direction(monster.field)
    print str(monster.field.x) + '_' + str(monster.field.y)

  def change_direction(self):
    return [True, False][randint(0, 1)]

  def random_direction(self, field):
    return field.keys[randint(0, len(field.keys))]