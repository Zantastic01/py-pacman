class GameListener:
  def on_game(self, game):
    while (False == game.is_ended()):
      self.eventDispatcher.dispatch('control', game)
      self.eventDispatcher.dispatch('rules', game)
      self.eventDispatcher.dispatch('view', game)
      self.eventDispatcher.dispatch('tick', game)