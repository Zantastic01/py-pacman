class Monster:
	def __init__(self, field):
		self.field = field
		print "Utworzylem potwora w " + str(self.field.x) + '_' + str(self.field.y)

	def set_field(self, field):
		self.field = field

	def set_shift(self, shift):
		self.shift = shift