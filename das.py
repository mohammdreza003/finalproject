# from room_node import Room_node
# این هنووز دایرکت اکسس تیبل نیست 
# هش فانکش رو درست کن که بشه باهاش سرچ کرد 
# اتاق ها 
class Array:
    def __init__(self, size=10):
        self.size = size
        self.arr = [None] * size
        self.i = 0

    def _hashf(self, item, func=lambda x: x.room_number):
        return func(item) % self.size
    def _hashf_s(self , item):
        return item % self.size

    def insert_a(self, item, func=lambda x: x.room_number):
        index = self._hashf(item ,func)
        # print(f"Inserting into Array: {item} at index {index}.")
        if self.arr[index] is None:
            self.arr[index] = item
            self.i += 1
            return True
        return False
# این رو درست کن 
    def search_a(self, data):
        index = self._hashf_s(data)
        if self.arr[index] is not None:
            return self.arr[index]
        return False
    
    def not_active_room(self):
        for i in range (self.size):
            if self.arr[i] is not None:
                if self.arr[i].status is False:
                    print(self.arr[i])

    # def change_status(self):
    #     pass
    
    def display_a(self):
        for i in range(self.size):
            if self.arr[i] is not None:
                print(self.arr[i])

    def display_a_for_costomer(self):
        for i in range(self.size):
            if self.arr[i] is not None and self.arr[i].status is True :
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
                self._insert_whtout_resize(item)

    def _resize_if_need(self):
        l_factor = (self.num_element) / self.size
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
        self.num_element +=1 
        return True
    def _is_slot_taken(self , index):
        return self.table[index] is not None
    
    def _next_index(self,index , i):
        return (index + i*i) % self.size
    
    def insert(self , key,item):
        self._resize_if_need()
        self._insert_whtout_resize(key , item)


    
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
                return self.table[index]
            
            index = self._next_index(index , i)
        return False
    
    

    def display(self):
        for i in range (self.size):
            if self.table[i] is not None:
                print(self.table[i])
            i+=1



#طبقه
# این باید قسمت ریسایز درست شه 
class Dynanichash2:
    def __init__(self):
        self.table = [None] * 19
        self.size = 19
        self.num_element = 0

    def _hash_function(self, key):
        return key % self.size

    def dat_in_hash(self):
        for i in range(self.size):
            self.table[i] = Array()

    def _rehash(self, new_size):
        old_table = self.table
        self.table = [None] * new_size
        self.size = new_size
        self.dat_in_hash()
        self._rehash_item(old_table)

    def _rehash_item(self, old_table):
        for array in old_table:
            if array is not None:
                for item in array.arr:
                    if item is not None:
                        self._insert(item)

    def _resize_if_need(self):
        l_factor = (self.num_element) / self.size
        if l_factor >= 0.75:
            self._rehash((self.size * 2))
        elif l_factor < 0.25 and self.size > 5:
            self._rehash((self.size // 2))

    def _insert(self, item, func=lambda x: x.floor):
        index = self._hash_function(func(item))
        if self.table[index] is None:
            self.table[index] = Array()
        if self.table[index].insert_a(item):
            self.num_element += 1

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

    def display_for_customer(self):
        for i in range (self.size):
            print(f"floor {i}:")
            if self.table[i] is not None:
                self.table[i].display_a_for_costomer()
            else:
                print("Empty")

    def not_active_room(self):
        for i in range(self.size):
            if self.table[i] is not None:
                self.table[i].not_active_room()
            i +=1


class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None


class Sll :
    def __init__(self) :
        self.head = None
        self.end = None


    def inserst_first(self , data):
       node = Node(data)
       if self.head is None :
            self.head = node
            self.end = node
       else:
            self.end = self.head
            self.head = node
            self.head.next  = self.end
            return True


    

    def remove_first(self):
        temp = self.head
        if temp is None:
            return
        self.head = temp.next

    

    def remove_data(self,data, func = lambda x : x):
        temp = self.head
        if not temp:
            return 'is empty!!!!!! ' 
            # badan falz kon



        if data == func  (temp.data):
            return self.remove_first()
        
        while temp.next :
            if data == func(temp.next. data):
                temp.next = temp.next.next
                return True
            temp = temp.next
        return False
        

    def search(self,data, func = lambda x : x ):
        
        temp = self.head
        while temp :
            if data == func(temp.data) :
                return temp.data
            temp = temp.next
        return False        
    def lenth(self):
        temp = self.head
        count = 0
        while temp :
            count = count+1 
            temp = temp .next
        return count


        

    
    def display(self):
        temp =  self.head
        while temp:
            print(temp.data, end='->')
            temp = temp.next
   


# s = Sll()
# s.inserst_first(1)
# s.inserst_first(2)
# s.inserst_first(3)
# s.inserst_first(5)

# s.display()
        

