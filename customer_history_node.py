class History_node:
    def __init__(self , room_number , start_time  , end_time , register):
        self.room_number = room_number
        self.start_time = start_time
        self.end_time = end_time
        self.register = register

    def __str__(self):
        return f'''
        room_number = {self.room_number}
        start_time = {self.start_time}
        end_time = {self.end_time}
        register = {self.register}
        
'''