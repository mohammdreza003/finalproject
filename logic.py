from das import Array , Daynamichashtable , Dynanichash2
from customer_node import Customer_node
from room_node import Room_node
from reserve_node import Reserve_node
from customer_history_node import History_node
import random
class Logic:
    # اینت رو درست کن 
    def __init__(self):
        self.room = Array()
        self.hash_customer = Daynamichashtable()
        self.floor = Dynanichash2()
    


    def customer_sign_in(self,key,val):
        x = self.hash_customer.search(key)
        if x :
            return False
        self.hash_customer.insert(key ,Customer_node(key , val))
        return True
    
    def customer_login(self,key,val):
        x = self.hash_customer.search_1(key , val)
        if x : 
            return True
        else:
            return False
        
    def manager_create_room(self,floor , bed , room_number ):
        # if self.room.search(room_number):
        #     return False
        # return self.room.insert(room_number , Room_node(x,bed,y,room_number))
        
        return self.floor.insert(Room_node(False , bed , False , room_number  , floor))
    def manager_display_all_room(self):
        return self.floor.display()
    
    def manager_display_all_customer(self):
        self.hash_customer.display()
    # این برا چیه ؟؟؟؟  |
    def manager_search_floor(self):
        pass
    def customer_search_with_floors(self,rangs_input):
        if rangs_input is None:
            self.manager_display_all_room()
        else:
            rangs_input = rangs_input.strip()
            ranges = rangs_input.split(',')
            for range in ranges:
                s = self.floor.search(int(range))
                if s:
                    s.display_a()

    def anager_display_in_floor(self,display_input):
        return self.floor.search(display_input)
    
    def manager_search_with_room_code(self,room_code):
        room_number = room_code %10
        floor = room_code // 100
        x = self.floor.search_with_room_code(floor , int(room_number))
        if x :
            return True
        else:
            return False
    def manager_not_active_room(self):
        return self.floor.not_active_room()
    
    def manager_change_status_room(self,room_code , new_status):
        room_number = room_code %10
        floor = room_code // 100
        x=self.floor.search_with_room_code(floor , room_number)
        x.status = new_status
        return True

    # customer 
    def customer_display(self):
        return self.floor.display_for_customer()

    def customer_book_room(self , room_code  , start_time , end_time ,key , val):
        x =self.check_full(room_code , start_time , end_time ,key , val)

        if x:
            return True
        else:
            return False
        

    def check_full(self,room_code , start_time , end_time , key , val):
        room_number = room_code %10 
        # bed = (room_code//10 ) %10
        floor = room_code //100 
        code =f'{random.randint(0 , 999999) : 06}'
        # print(f'your register code :{code}')
        x =self.floor.search_with_room_code(floor , room_number)
        if x:
            if x.status == True:
                if x.time_reserve.head is None:
                    return self.customer_node_update( x,room_code , start_time , end_time , key , val , code)

                elif  x.time_reserve.end_time < start_time :
                    return self.customer_node_update( x,room_code , start_time , end_time  , key , val , code)
                else:
                    return False
            return False
    def customer_node_update(self , x,room_code , start_time , end_time , key , val , code):
            x.time_reserve.inserst_first(Reserve_node(room_code , start_time , end_time , code))
            x =self.hash_customer.search_1(key , val)
            if x :
                x.history.inserst_first(History_node(room_code , start_time , end_time , code))
                return True  , f'your register code {code}'
            else:
                return False
            
    

    