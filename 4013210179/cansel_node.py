class Cansel_node:
    def __init__(self , register , reason):
        self.register = register
        self.dalil = reason

    def __str__(self):
        return f''' 
        this room with this register code{self.register} with this reason {self.dalil} has canseled .

''' 
        