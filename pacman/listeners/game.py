class GameListener:
  def on_game(self, game):
    eventDispatcher = game.eventDispatcher

    while (False == game.is_ended()):
      eventDispatcher.dispatch('control', game)
      eventDispatcher.dispatch('rules', game)
      eventDispatcher.dispatch('view', game)
      eventDispatcher.dispatch('tick', game)