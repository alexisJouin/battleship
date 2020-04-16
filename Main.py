#NOTE : 
# O : zone vide
# X : zone tirée
# B : zone avec Bateau
# T : Zone touchée

from Board import Board;
from Ship import Ship;
from Case import Case;

boardJ1 = Board("J1")
boardJ2 = Board("J2")
players = [boardJ1, boardJ2]

boardJ1.display()

print("BatleShip Python !!")
print("Appuyer sur q pour quitter")
end = 1

while(end==1):
    for player in players:
        print("**************************")
        print("Joueur ", player.name)
        print("Placement des bateaux (Aléatoire) ...")
        
        player.placeShipsRandom()
        
        for ship in player.ships:
            ship.display()
        
       
        
    #Début de la partie
    for player in players:
        print("**************************")
        print("Joueur ", player.name)
        nbShips = len(player.ships)
        player.display()
       
    
        print(nbShips, " bateau(x) restant(s)")
        choix = input("Attaquer : ") 
        
        
        
        
        if(choix == "q"):
            print("Partie arrêtée ...")
            end = 0
            break
    
    
    
    
        if nbShips == 0:
            print(" a perdu !")
            end = 0
            break
        
    if(choix == "q"):
        print("Partie arrêtée ...")
        end = 0
        break
    
        
    