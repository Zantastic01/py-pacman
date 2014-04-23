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
	board = []
	ended = False

	def __init__(self):
		self.initListeners()
		self.gameListeners()

	def start(self):
		self.eventListener.dispatch('init', self)
		self.eventListener.dispatch('game', self)

	def initListeners(self):
		self.eventListener.add('init', PacmanInitListener(), 'onInit')
		self.eventListener.add('init', BoardInitListener(), 'onInit')
		self.eventListener.add('init', MonsterInitListener(), 'onInit')
		self.eventListener.add('game', GameListener(), 'onGame')

	def gameListeners(self):
		self.controlListeners()
		self.rulesListeners()
		self.viewListeners()

	def controlListeners(self):
		self.eventListener.add('control', MonsterCtrlListener(), 'onControl')
		self.eventListener.add('control', PacmanCtrlListener(), 'onControl')

	def rulesListeners(self):
		self.eventListener.add('rules', EndGameListener(), 'onRules')

	def viewListeners(self):
		self.eventListener.add('view', PygameViewListener(), 'onView')

	def isEnded(self):
		return self.ended


