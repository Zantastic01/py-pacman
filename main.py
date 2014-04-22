from Board import *

board = SimpleBoard().getBoard()

fi = board.get(8, 1)
print str(fi.x) + ' ' + str(fi.y) + ' ' + fi.fieldType
fi2 = fi.getBottom()
print str(fi2.x) + ' ' + str(fi2.y) + ' ' + fi2.fieldType
fi3 = fi2.getBottom()
print str(fi3.x) + ' ' + str(fi3.y) + ' ' + fi3.fieldType
fi4 = fi3.getLeft()
print str(fi4.x) + ' ' + str(fi4.y) + ' ' + fi4.fieldType
