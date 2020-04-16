#0 : case non endommagée
#1 : case endommagée

class Ship(object):
    def __init__(self, cases):
        
        self.etat = "alive"
        self.cases = []
        for case in cases:
            self.cases.append(case)
        
    
    def display(self):
        print("Bateau : ", self.etat)
        for case in self.cases:
            print(case.col, case.lign, " : ", case.etat)