class GameListener:
  def onGame(self, game):
    eventListener = game.eventListener

    while (False == game.isEnded()):
      eventListener.dispatch('control', game)
      eventListener.dispatch('rules', game)
      eventListener.dispatch('view', game)