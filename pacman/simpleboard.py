from loadboard import *

class SimpleBoard(LoadBoard):
  rawBoard = [
      [0,  0,   0,    0,  0,  0,  0,   0,   0,  0],
      [0, 246, 34,  234, 34, 34, 34, 34,  23,  0],
      [0,  12,  0,   12,  0,  0,  0,   0, 125,  0],
      [0,  14, 34,  134, 34, 34, 34,  34,  13,  0],
      [0,   0,  0,    0,  0,  0,  0,   0,   0,  0]
    ]
  def __init__(self):
    LoadBoard.__init__(self, self.rawBoard)