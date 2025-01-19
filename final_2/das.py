# from room_node import Room_node
# این هنووز دایرکت اکسس تیبل نیست 
# هش فانکش رو درست کن که بشه باهاش سرچ کرد 
# اتاق ها 
class Array:
    def __init__(self, size=10):
        self.size = size
        self.arr = [None] * size
        self.i = 0

    
    
    def insert(self, item, func=lambda x: x.room_number):
        
        # print(f"Inserting into Array: {item} at index {index}.")
        if self.arr[func(item)] is None:
            self.arr[func(item)] = item
            self.i += 1
            return True
        return False
# این رو درست کن 
    def search_a(self, data):
        if self.arr[data] is not None:
            return self.arr[data]
        return False
    
    
    # def change_status(self):
    #     pass
    
    def display_a(self):
        for i in range(self.size):
            if self.arr[i] is not None:
                print(self.arr[i])
# لامدا رو درست کن برای این 
# قسمت ریساز باید برای این درست شه


class Daynamichashtable:
    def __init__(self):
        self.table =  [None] * 29
        self.size = 29 
        self.num_element  = 0 

    def _hash_function(self, key, func = lambda x:x):
        a = 0.6188033
        return int(self.size * ((func(key) * a) %1))
    
    def _rehash(self, new_size):
        old_table = self.table
        self.table = [None] * new_size
        self.size = new_size
        self.num_element = 0
        self._rehash_item(old_table)

    def _rehash_item(self , old_table):
        for item in old_table:
            if item is not None:
                self._insert_wthout_resize(item)

    def _resize_if_need(self):
        l_factor = (self.num_elment) / self.size
        if l_factor >=0.75:
            self._rehash(self.size *2)
        elif l_factor < 0.25 and self.size > 5:
            self._rehash(self.size // 2)

    def _insert_whtout_resize(self , key , item ):
        index = self._hash_function(key) 
        i = 0 
        while self._is_slot_taken(index):
            if self.table[index] == item:
                return False
            i +=1 
            index = self._next_index(index , i)
        self.table[index] = item
        self.num_elment +=1 
        return True
    def _is_slot_taken(self , index):
        return self.table[index] is not None
    
    def _next_index(self,index , i):
        return (index + i*i) % self.size
    
    def insert(self , key,item):
        self._resize_if_need()
        return self._insert_whtout_resize(key , item)
    
    def search(self , key):
        index = self._hash_function(key)
        for i in range(self.size):
            if self.table[index] and self.table[index].key == key:
                return self.table[index]
            
            index = self._next_index(index , i)
        return False
    
    def search_1(self , key , val):
        index = self._hash_function(key)
        for i in range(self.size):
            if self.table[index] and self.table[index].key == key and self.table[index].val == val:
                return True
            
            index = self._next_index(index , i)
        return False
    
    

    def display(self):
        for item in self.table:
            return item




#طبقه
# این باید قسمت ریسایز درست شه 
class Dynanichash2:
    def __init__(self):
        self.table = [None] * 19
        self.size = 19
        self.num_element = 0

    def _hash_function(self, key ):
        return key % self.size

    def _rehash(self, new_size):
        old_table = self.table
        self.table = [None] * new_size
        self.size = new_size
        self._rehash_item(old_table)

    def _rehash_item(self, old_table):
        for item in old_table:
            if item is not None:
                self._insert(item)

    def _resize_if_need(self):
        l_factor = (self.num_element) / self.size
        if l_factor >= 0.75:
            self._rehash((self.size * 2))
        elif l_factor < 0.25 and self.size > 5:
            self._rehash((self.size // 2))

    def _insert(self, item):
        index = self._hash_function((item))
        self.table[index] = item
        self.num_element =+1
        return True

            
        

    def insert(self, item):
        self._insert(item)
        self._resize_if_need()


    def search(self, item):
        index = self._hash_function(item)
        if self.table[index] is not None:
            self.table[index].display_a()

    def search_with_room_code(self , floor , room_number):
        index = self._hash_function(floor)
        if self.table[index] is not None:
            return self.table[index].search_a(room_number)
        return False

    def display(self):
        for i in range(self.size):
            print(f"floor {i}:")
            if self.table[i] is not None:
                self.table[i].display_a()
            else:
                print("Empty")

    def not_active_room(self):
        for i in range(self.size):
            if self.table[i] is not None:
                self.table[i].not_active_room()
            i +=1

   




        

