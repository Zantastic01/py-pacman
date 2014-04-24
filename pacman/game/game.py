from eventlistener import *

from listeners import *
from ..pacman.listeners import *
from ..board.listeners import *
from ..monster.listeners import *

# init
# game
# 	control
# 		MonsterCtrl
# 		PacmanCtrl
# 	rules
# 		EndGameRule
# 	view
# 		PygameView
# 	next
# 		if game.end == false
# 			game


class Game:
	eventListener = EventListener();
	monsters = []
	pacman = []
	board = None
	ended = False
	view = None

	def __init__(self):
		self.initListeners()
		self.gameListeners()

	def start(self):
		self.eventListener.dispatch('init', self)
		self.eventListener.dispatch('game', self)

	def initListeners(self):
		self.eventListener.add('init', BoardInitListener(), 'on_init')
		self.eventListener.add('init', PacmanInitListener(), 'on_init')
		self.eventListener.add('init', MonsterInitListener(), 'on_init')
		self.eventListener.add('game', GameListener(), 'on_game')

	def gameListeners(self):
		self.controlListeners()
		self.rulesListeners()
		self.viewListeners()

	def controlListeners(self):
		self.eventListener.add('control', MonsterCtrlListener(), 'on_control')
		self.eventListener.add('control', PacmanCtrlListener(), 'on_control')

	def rulesListeners(self):
		self.eventListener.add('rules', EndGameListener(), 'on_rules')

	def viewListeners(self):
		self.eventListener.add('view', PygameViewListener(), 'on_view')

	def isEnded(self):
		return self.ended


