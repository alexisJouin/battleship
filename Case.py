class Case(object):
    def __init__(self, case):
        self.col = str(case[0])
        
        #Conversion de list en int
        strings = [str(integer) for integer in case[1:]]
        a_string = "".join(strings)
        lign = int(a_string)
        
        self.lign = int(lign)
        self.etat = ""