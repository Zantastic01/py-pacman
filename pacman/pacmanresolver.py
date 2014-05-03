from pacman import *

class PacmanResolver:
  def __init__(self, board, pacman):
    self.board = board
    self.pacman = pacman

  def resolve(self):
    for pacman in self.pacman:
      field = self.board.get(pacman[0], pacman[1])
      pacman = Pacman(field)
      field.add_animal(pacman)
