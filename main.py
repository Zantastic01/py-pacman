from Board import *

board = SimpleBoard().get_board()

fi = board.get(8, 1)
print str(fi.x) + ' ' + str(fi.y) + ' ' + fi.fieldType
fi2 = fi.get_bottom()
print str(fi2.x) + ' ' + str(fi2.y) + ' ' + fi2.fieldType
fi3 = fi2.get_bottom()
print str(fi3.x) + ' ' + str(fi3.y) + ' ' + fi3.fieldType
fi4 = fi3.get_left()
print str(fi4.x) + ' ' + str(fi4.y) + ' ' + fi4.fieldType
