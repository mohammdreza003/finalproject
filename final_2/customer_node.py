# کلید شماره ملی کاربر هست 

class Customer_node:
    def __init__(self , key , val):
        self.key  = key 
        self.val = val 
        self.cansel_counter = 0

    def __str__(self):
        return f''' 
        key  : {self.key}
        val  : {self.val}
        cansel_counter = {self.cansel_counter}
    '''