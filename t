 #def auto_reserve(self , key , val):
    #     bed = int(input('enter how many bed you want :'))
    #     # start_year =  int(input('enter year for resrvaiton start:'))
    #     # start_month = int(input('enter month for resrvaiton start'))
    #     # start_day = int(input('enter day resrvaiton start'))
    #     # start_time = self.time.access(start_year  , start_month , start_day)
    #     # end_year = int(input('enter year to reservtion end :'))
    #     # end_month = int(input('enter month resrvaiton end'))
    #     # end_day = int(input('enter day resrvaiton end'))
    #     # end_time = self.time.access(end_year , end_month , end_day)
    #     start_time = int(input('enter start time:'))
    #     end_time = int(input('enter end time :'))
    #     code =f'{random.randint(0 , 999999) : 06}'
    #     x=self.logic.auto_reserve(key ,bed , start_time , end_time , code , val)
    #     if x :
    #          print(f' your register code is this : {code}')
        
 # def auto_reserve(self,key ,bed , start_time , end_time , code , val):
    #     x = self.floor.search_auto(int(bed))
    #     print(x)
    #     if x.full == False and x.status == True :
    #         if x.time_reserve.head is None:
    #             room_code = x.room_code
    #             x.time_reserve.inserst_first(Reserve_node_into_room(room_code , start_time , end_time , code ))
    #             x = self. hash_customer.search_1(key , val)
    #             if x :
    #                 x.history.inserst_first(History_node(room_code , start_time , end_time , code))
    #                 self.reserve_room.insert(int(code) ,Reserve_node_a(code , room_code,start_time , end_time , key))
    #                 return True

    #         if x.time_resreve.end_time<end_time :
    #             x.full = True
    #             room_code = x.room_code
    #             x.time_reserve.inserst_first(Reserve_node_into_room(room_code , start_time , end_time , code ))
    #             o = self. hash_customer.search_1(key , val)
    #             if o :
    #                 o.history.inserst_first(History_node(room_code , start_time , end_time , code))
    #                 self.reserve_room.insert(int(code) ,Reserve_node_a(code , room_code,start_time , end_time , key))
    #                 return True
