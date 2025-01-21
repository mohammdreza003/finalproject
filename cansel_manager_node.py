class Cansel_node_manager:
    def __init__(self , key , reason , register):
        self.username = key
        self.reson = reason
        self.register = register

    def __str__(self):
        
        return f'''
            username = {self.username}
            reason = {self.reson}
            register code = {self.register}
        '''