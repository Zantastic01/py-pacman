from ...listener import *
from ...monster import *
from endgame import *
from datetime import *

class FruitPowerListener(Listener):
  def on_rules(self, game):
    pacman = game.pacman[0]
    fruit = pacman.field.fruit

    if fruit != None and fruit.eaten == False:
      fruit.eaten = True
      pacman.fruits += 1
      self.activate_fruit_mode(game)
      self.start = datetime.today()
      
  def on_rules_fruitmode(self, game):
      pacman = game.pacman[0]

      monsterCollisions = Rules().get_collision(pacman, Monster)
      if len(monsterCollisions) > 0:
        for monster in monsterCollisions:
          pacman.monsters += 1
          monster.field.animals.remove(monster)
          game.monsters.remove(monster)

      stop = datetime.today()
      interval = stop - self.start
      if interval.seconds >= 20:
        self.deactivate_fruit_mode(game)

  def activate_fruit_mode(self, game):
    self.eventDispatcher.remove('rules', {
      'listener': eval('EndGameRuleListener'),
      'method': 'on_rules'
    })
    self.eventDispatcher.add('rules', self, 'on_rules_fruitmode')

    for monster in game.monsters:
      monster.active = False

  def deactivate_fruit_mode(self, game):
      self.eventDispatcher.remove('rules', {
        'listener': eval('FruitPowerListener'),
        'method': 'on_rules_fruitmode'
      })
      self.eventDispatcher.add('rules', EndGameRuleListener(), 'on_rules')

      for monster in game.monsters:
        monster.active = True
