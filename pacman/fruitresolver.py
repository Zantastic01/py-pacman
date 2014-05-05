from fruit import *

class FruitResolver:
  def __init__(self, board, fruits):
    self.board = board
    self.fruits = fruits

  def resolve(self):
    for fruit in self.fruits:
      field = self.board.get(fruit[0], fruit[1])
      field.fruit = Fruit(fruit[2])