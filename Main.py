#NOTE : 
# O : zone vide
# X : zone tirée
# B : zone avec Bateau
# T : Zone touchée

from Board import Board;


boardJ1 = Board()
boardJ2 = Board()

boardJ1._setName("J1")
boardJ1._setName("J2")



print(boardJ1._getValue())
print(boardJ2._getValue())

boardJ1.shoot("d", 9)
boardJ1.placeShip([["d", 9],["d",8]])
#boardJ1.placeShip([["d", 9],["d",8]])

print(boardJ1._getValue())