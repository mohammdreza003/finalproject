from das import Array , Dynanichash2
from room_node import Room_node
class Logic:
    def __init__(self):
        self.room = Array()
        self.floor = Dynanichash2()
        for i in range(self.floor.size):
            self.floor.table[i] = self.room
            i+=1 

    def manager_create_room (self , floor , bed , room_number):
        self.floor.insert(floor)
        self.arr.insert(Room_node(False , bed , False  , room_number , floor ))