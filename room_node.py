from das import Sll
class Room_node:
    def __init__(self,status , number_of_beds,full,room_number,floor ):
        self.status  = status 
        self.number_of_bed = number_of_beds
        self.full = full
        self.room_number = room_number
        self.floor = floor
        self.time_reserve = Sll()
        

    def __str__(self):
        return f''' 
        status = {self.status}
        number of bed = {self.number_of_bed}
        full = {self.full}
        room number = {self.room_number}
        floor = {self.floor}
        time_reserve = {self.time_reserve.display()}
        '''     
    # def display(self):
    #     print(f'{self.status} , {self.number_of_bed} , {self.full}')