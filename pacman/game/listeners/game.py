class GameListener:
  def on_game(self, game):
    eventListener = game.eventListener

    while (False == game.isEnded()):
      eventListener.dispatch('control', game)
      eventListener.dispatch('rules', game)
      eventListener.dispatch('view', game)