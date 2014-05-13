from eventdispatcher import *
from listeners import *

class Game:
	eventDispatcher = EventDispatcher();
	lifes = 3
	monsters = []
	pacman = []
	board = None
	ended = False
	view = None
	maxDots = 0
	maxFruits = 0

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
		self.eventDispatcher.add('pacman_collision', endGameRuleListener, 'on_pacman_collision')
		self.eventDispatcher.add('keypressed', endGameRuleListener, 'on_keypressed')
		self.eventDispatcher.add('end_game', endGameRuleListener, 'on_end_game')

		self.eventDispatcher.add('rules', FruitPowerListener(), 'on_rules')

	def view_listeners(self):
		self.eventDispatcher.add('view', ViewListener(), 'on_view')

		self.eventDispatcher.add('draw_info', ScoreViewListener(), 'on_draw_info')
		self.eventDispatcher.add('draw_info', LifeViewListener(), 'on_draw_info')

		fruitViewListener = FruitViewListener()
		self.eventDispatcher.add('draw_info', fruitViewListener, 'on_draw_info')

		self.eventDispatcher.add('draw_element', EmptyViewListener(), 'on_draw_element')
		self.eventDispatcher.add('draw_element', WallViewListener(), 'on_draw_element')
		self.eventDispatcher.add('draw_element', DotViewListener(), 'on_draw_element')
		self.eventDispatcher.add('draw_element', fruitViewListener, 'on_draw_element')

		self.eventDispatcher.add('draw_animal', PacmanViewListener(), 'on_draw_animal')
		self.eventDispatcher.add('draw_animal', MonsterViewListener(), 'on_draw_animal')

		messagesViewListener = MessagesViewListener()
		self.eventDispatcher.add('pacman_win', messagesViewListener, 'on_pacman_win')
		self.eventDispatcher.add('pacman_lost', messagesViewListener, 'on_pacman_lost')
		self.eventDispatcher.add('init', messagesViewListener, 'on_init')
		self.eventDispatcher.add('pacman_lost_life', messagesViewListener, 'on_pacman_lost_life')

	def is_ended(self):
		return self.ended
