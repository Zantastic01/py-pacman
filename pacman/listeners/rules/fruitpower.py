class FruitPowerListener(Listener):
  def on_rules(self, game):
    pacman = game.pacman[0]
    fruit = pacman.field.fruit

    if fruit != None and fruit.eaten == False:
      for listener in self.eventDispatcher.listeners['rules']:
        if isinstance(listener, EndGameRuleListener):
          self.eventDispatcher.listeners['rules'].remove(listener)

      for monster in game.monsters:
        monster.active = False

      

      start 20s
      pin game rule
      normalize monsters
