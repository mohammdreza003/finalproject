class Reserve_node_a:
    def __init__(self , room_code , start_time , end_time , code , key):
        self.room_code = room_code
        self.start_time = start_time
        self.end_time = end_time
        self.register = code
        self.useername_to_reserv = key

    def __str__(self):
        return f''' 
        room_code = {self.room_code}
        self.start = {self.start_time}
        endd_time = {self.end_time}
        register code = {self.register}
        username reserved = {self.useername_to_reserv}
'''