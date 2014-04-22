from eventlistener import *
from ..pacman.listeners import *
from ..monster.listeners import *
from ..board.listeners import *

class Game:
	monsters = []
	pacman = []
	board = []

	def __init__(self):
		self.eventListener = EventListener();
		self.addBoardListeners()
		self.addPacmanListeners()
		self.addMonsterListeners()
		self.addInitListeners()

	def addBoardListeners(self):
		self.eventListener.add('game.init', InitBoardListener, 'onInit')
		
	def addPacmanListeners(self):
		self.eventListener.add('game.init.add_pacman', AddPacmanListener, 'onInit')

	def addMonsterListeners(self):
		self.eventListener.add('game.init.add_monster', AddMonsterListener, 'onInit')

	def addInitListeners(self):
		self.eventListener.add('game.init', InitBoardListener, 'onInit')