# کلید شماره ملی کاربر هست 
from das import Sll

class Customer_node:
    def __init__(self , key , val):
        self.key  = key 
        self.val = val 
        self.cansel_counter = 0
        self.history = Sll()

    def __str__(self):
        return f''' 
        key  : {self.key}
        val  : {self.val}
        cansel_counter = {self.cansel_counter}
        history  : {self.history.display()}
    '''