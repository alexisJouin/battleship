from Case import Case;
from Ship import Ship;

class Board(object):
    def __init__(self, name):
        
        self.name = name
        self.board = []
        self.ships = []
        
        #Initialisation du plateau
        colInt = ord("A")
        for i in range(1,11):
            for j in range(1,11):
                col = chr(colInt + j - 1)
                self.board.append(Case([col,i]))
        
    
    def _setName(self, name):
        self.name = name
        
    def _getName(self):
        return self.name
    
    def uploadCase(self, case):
        print(self.board.index(case.col))
    
    def display(self):
        for case in self.board:
            print(case.col, case.lign, " : ", case.etat, " - case n° : ", case)
            
    def displayShips(self):
        for ship in self.ships:
            ship.display()
    
    def shoot(self, case):
        if(self.board[self.board.index(self.foundCase(case))].etat == ""):
            self.board[self.board.index(self.foundCase(case))].etat = "X"
        elif(isinstance(self.board[self.board.index(self.foundCase(case))].etat, Ship())):
            self.board[self.board.index(self.foundCase(case))].etat = "T"
    
    def upload(self):
        for ship in self.ships:
            for case in ship.cases:
                self.board[self.board.index(case)].etat = ship
    
    def placeShipsRandom(self):
        ship1 = Ship([self.foundCase("A1"),self.foundCase("A2"),self.foundCase("A3")])
        ship2 = Ship([self.foundCase("C5"),self.foundCase("C6")])
        ship3 = Ship([self.foundCase("J9"),self.foundCase("I9"),self.foundCase("H9")])
        ship4 = Ship([self.foundCase("C10")])
        self.ships.append(ship1)
        self.ships.append(ship2)
        self.ships.append(ship3)
        self.ships.append(ship4)
        
        self.upload()
    
    #Retourne l'adresse de l'objet Case de la case correspondante en valeur
    def foundCase(self, caseU):
        
        #Conversion de list en int
        strings = [str(integer) for integer in caseU[1:]]
        a_string = "".join(strings)
        lignU = int(a_string)
        
        for case in self.board:
            if(case.col == caseU[0]):
                if(case.lign == lignU):   
                    return case
                

        