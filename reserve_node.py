class Reserve_node:
    def __init__(self , room_code,start_time , end_time , register):
        self.room_code =room_code
        self.statrt_time = start_time
        self.end_time   = end_time
        self.register = register

    def __str__(self):
        return f''' 
        room_code = {self.room_code}
        sstart_time = {self.statrt_time}
        end_time = {self.end_time}
        register code = {self.register}
'''
    