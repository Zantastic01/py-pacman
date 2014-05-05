from eventdispatcher import *
from listeners import *

class Game:
	eventDispatcher = EventDispatcher();
	monsters = []
	pacman = []
	board = None
	ended = False
	view = None
	maxDots = 0

	def __init__(self):
		self.init_listeners()
		self.game_listeners()

	def start(self):
		self.eventDispatcher.dispatch('init', self)
		self.eventDispatcher.dispatch('game', self)

	def init_listeners(self):
		self.eventDispatcher.add('init', BoardInitListener(), 'on_init')
		self.eventDispatcher.add('init', ViewInitListener(), 'on_init')
		self.eventDispatcher.add('game', GameListener(), 'on_game')

	def game_listeners(self):
		self.control_listeners()
		self.rules_listeners()
		self.view_listeners()
		self.eventDispatcher.add('tick', TickRuleListener(), 'on_tick')

	def control_listeners(self):
		self.eventDispatcher.add('control', KeyControlListener(), 'on_control')
		self.eventDispatcher.add('control', MonsterControlListener(), 'on_control')

		pacmanControlListener = PacmanControlListener()
		self.eventDispatcher.add('control', pacmanControlListener, 'on_control')
		self.eventDispatcher.add('keypressed', pacmanControlListener, 'on_keypressed')

	def rules_listeners(self):
		self.eventDispatcher.add('rules', ShiftAnimalRuleListener(), 'on_rules')

		endGameRuleListener = EndGameRuleListener()
		self.eventDispatcher.add('rules', endGameRuleListener, 'on_rules')
		self.eventDispatcher.add('keypressed', endGameRuleListener, 'on_keypressed')
		self.eventDispatcher.add('end_game', endGameRuleListener, 'on_end_game')

	def view_listeners(self):
		self.eventDispatcher.add('view', ViewListener(), 'on_view')
		self.eventDispatcher.add('draw_wall', WallViewListener(), 'on_draw')
		self.eventDispatcher.add('draw_empty', EmptyViewListener(), 'on_draw')
		self.eventDispatcher.add('draw_dot', DotViewListener(), 'on_draw')
		self.eventDispatcher.add('draw_animal', AnimalViewListener(), 'on_draw')

	def is_ended(self):
		return self.ended
