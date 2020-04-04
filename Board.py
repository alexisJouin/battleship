# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:48:28 2020

@author: alexi
"""

class Board(object):
    def __init__(self):
        
        self.name = "board"
        self.value = {
            "a" : [1,2,3,4,5,6,7,8,9,10],
            "b" : [1,2,3,4,5,6,7,8,9,10],
            "c" : [1,2,3,4,5,6,7,8,9,10],
            "d" : [1,2,3,4,5,6,7,8,9,10],
            "e" : [1,2,3,4,5,6,7,8,9,10],
            "f" : [1,2,3,4,5,6,7,8,9,10],
            "g" : [1,2,3,4,5,6,7,8,9,10],
            "h" : [1,2,3,4,5,6,7,8,9,10],
            "i" : [1,2,3,4,5,6,7,8,9,10],
            "j" : [1,2,3,4,5,6,7,8,9,10],
        }
        
        for i in self.value:
            for j in range(10):
                self.value[i][j] = "O"
        
    
    def _setName(self, name):
        self.name = name
        
    def _getName(self):
        return self.name
    
    def _setValue(self, value):
        self.value = value
        
    def _getValue(self):
        return self.value
        
    def shoot(self, i,j):
        self.value[i][j]= "X"
    
    def placeShip(self, coords):
        for coord in coords:
            if(coord[0] != "B" and (coord[0] >="A" and coord[0]<="J" )):
                if(coord[1] != "B"):
                    self.value[coord[0]][coord[1]]= "B"
                else:
                    print("Erreur, déjà un bateau présent ou hors du plateau !")
                
            else:
                print("Erreur, déjà un bateau présent ou hors du plateau !")
        