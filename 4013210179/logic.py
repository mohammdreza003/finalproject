from das import Array , Daynamichashtable , Dynanichash2 , Sll
from customer_node import Customer_node
from room_node import Room_node
from reserve_node import Reserve_node_into_room
from customer_history_node import History_node
from reserv_node_a import Reserve_node_a
from cansel_node import Cansel_node
from cansel_manager_node import Cansel_node_manager
from block_list import Block_list
from datetime import datetime
class Logic:
    # اینت رو درست کن 
    def __init__(self):
        # self.room = Array()
        self.hash_customer = Daynamichashtable()
        self.floor = Dynanichash2()
        self.reserve_room  = Daynamichashtable()
        self.reson1  = Sll()
        self.reson2 = Sll()
        self.reson3 = Sll()
        self.block_list = Sll()
    


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
        
    def manager_create_room(self,floor , bed , room_number , room_code ):
        # if self.room.search(room_number):
        #     return False
        # return self.room.insert(room_number , Room_node(x,bed,y,room_number))
        
        return self.floor.insert(Room_node(False , bed , False , room_number  , floor , room_code))
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

    def customer_book_room(self , room_code  , start_time , end_time ,key , val , code):
        x =self.check_full(room_code , start_time , end_time ,key , val , code)

        if x:
            return True
        else:
            return False
        

    def check_full(self,room_code , start_time , end_time , key , val , code):
        room_number = room_code %10 
        # bed = (room_code//10 ) %10
        floor = room_code //100 
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
            x.full = True
            x.time_reserve.inserst_first(Reserve_node_into_room(room_code , start_time , end_time , code))
            x =self.hash_customer.search_1(key , val)
            if x :
                x.history.inserst_first(History_node(room_code , start_time , end_time , code))
                self.reserve_room.insert(int(code) ,Reserve_node_a(code , room_code,start_time , end_time , key))
                return True 
            else:
                return False
            
    def cansel(self, register,x , key , val ):
        k = self.hash_customer.search_1(key , val)
        if k :
            k.history.remove_first()
            k.canseled.inserst_first(Cansel_node(register,x))
            k.cansel_counter =+1
            if k.cansel_counter == 3 :
                self.block_list.inserst_first(key)

            if x == 'change plan':
                self.reson1.inserst_first(Cansel_node_manager(key , x , register))   
            elif x == 'change place' :
                self.reson2.inserst_first(Cansel_node_manager(key , x , register))
            elif x == 'other cases':
                self.reson3.inserst_first(Cansel_node_manager(key , x , register))
            return True
        
        return False
    
    def customer_history(self , key , val):
        x = self.hash_customer.search_1(key , val)
        if x :
            return x
        return False
    
    def change_pass(self, key , ne_pass):
        x=self.hash_customer.search(key)
        if x:
            x.val = ne_pass
            return True
        return False
    
    def display_history_room(self , room_code):
        room_number = room_code %10 
        # bed = (room_code//10 ) %10
        floor = room_code //100 
        return self.floor.search_with_room_code(floor , room_number)        
    
    def display_reserve_baze(self, start_baze , end_baze):
        
        for i in range (self.reserve_room.size):
            if self.reserve_room.table[i] is not None and start_baze<= self.reserve_room.table[i].start_time and end_baze >= self.reserve_room.table[i].end_time :
                print(self.reserve_room.table[i])
            i=+1


    def display_canseld(self  , x):
        if x == 1:
            self.reson1.display()
        elif x == 2:
            self.reson2.display()
        elif x == 3:
            self.reson3.display()

    def display_manager_block(self):
        return self.block_list.display()
    def unblock(self , key):
        x=self.block_list.search(key)
        if x :
            self.block_list.remove_data(key)
            t=self.hash_customer.search(key)
            if t :
                t.cansel_counter = 0
                return True
            
        return False
    
    def auto_reserve(self,key ,bed , start_time , end_time , code , val):
        for i in range (self.floor.size):
            if self.floor.table[i].number_of_bed == bed and self.floor.table[i].floor is False and self.floor.table[i].status == True:
                if self.floor.table[i].time_reserve.end_time < end_time:
                    self.floor.table[i].full = True
                    room_code=self.floor.table.room_code
                    self.floor.table[i].time_reserve.inserst_first(Reserve_node_into_room(room_code , start_time , end_time , code ))
                    x = self. hash_customer.search_1(key , val)
                    if x :
                        x.history.inserst_first(History_node(room_code , start_time , end_time , code))
                        self.reserve_room.insert(int(code) ,Reserve_node_a(code , room_code,start_time , end_time , key))
                        return True
            i+=1




