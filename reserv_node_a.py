class Reserve_node_a:
    def __init__(self , key , room_code , start_time , end_time , code):
        self.key = key 
        self.room_code = room_code
        self.start_time = start_time
        self.end_time = end_time
        self.code = code

    def __str__(self):
        return f''' 
            register = {self.key}
            room_code = {self.room_code}
            start time = {self.start_time}
            end time = {self.end_time}
            username  = {self.code}
'''