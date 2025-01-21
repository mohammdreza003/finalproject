import random
from time1 import Time_l
class Interface:
    def __init__(self,logic):
        self.logic = logic
        self.time = Time_l()
    # کنترل ورودی ها یادت نره 
    #  مشتری سرچ بازی ای نداره یادت باشه 
    def menu(self):
        while True:
            menu = int(input('''
            ____menu____
            1 . customer panel
            2. manager panel
            3.exit
            '''))
            if menu == 1:
                self.customer_panel()
            elif menu == 2:
                self.manager_panel()
            elif menu == 3:
                return


    def customer_panel(self):
        while True:
            customer_menu = int(input(''' 
            __customer menu __
            1.sign in 
            2.login
            3.exit
             '''))
            if  customer_menu == 1:
                self.customer_sign_in()
            elif customer_menu == 2:
                self.customer_login()
            elif customer_menu == 3:
                break

            

            
    def manager_panel(self):
        while True :
            manager_menu  = int(input('''
            _manager menu_
            1.login 
            2.create room
            3.display all room
            4. display all customer
            5. search with room_code 
            6.display all room in floor
            7.display not active room   
            8. change status room 
            9.  display history of room 
            10. display reserve baze 
            11 .  display all cansel reserved 
            12. display customer in block list    
            13. exit
             '''))
            
            if manager_menu == 1:
                self.manager_sign_in()

            elif manager_menu == 2 :
                self.manager_create_room()

            elif manager_menu == 3:
                self.manager_display_all_room()

            elif manager_menu == 4 :
                self.manager_display_all_customer()

            elif manager_menu == 5:
                self.manager_search_with_room_code()

            elif manager_menu == 6:
                self.manager_display_in_floor()
            
            elif manager_menu ==7 :
                self.manager_not_active_room()
            
            elif manager_menu == 8:
                self.manager_change_status_room()

            elif manager_menu == 9:
                self.display_history_room()
            elif manager_menu == 10:
                self.display_reserve_baze()

            elif manager_menu == 11:
                self.manager_display_canseled()
            elif manager_menu == 12:
                self.display_manager_block()
            elif manager_menu == 13 :
                break

            
                
            
    def customer_sign_in(self):
        key = int(input('plaese enter your na_code for be your username to sign in :'))
        val = input('enter password you want :')
        x = self.logic.customer_sign_in(key,val)
        if x : 

                self.customer_log(key , val)
        else:
            print('this username alread exist !!!')

    def customer_login(self):
        key = int(input('enter your username:'))
        val = input('inter your pasword:')
        x=self.logic.customer_login(key , val)
        if x :
            self.customer_log(key , val)
        else:
            print('no')

    def customer_log(self , key , val):
         while True:

                customer_menu2 = int(input(''' 
                    __customer menu __
                    1.display all room in floor
                    2.book room
                    3.cansel reserve
                    4. display history reserve
                    5. change password
                    6.auto reserve
                    7.exit
                '''))

                if customer_menu2 == 1:
                    self.customer_display_in_floor()

                elif customer_menu2 == 2:
                    self.customer_book_room(key , val)

                elif customer_menu2 == 3 : 
                    self.cansel_reserve(key , val)

                elif customer_menu2 == 4 :
                    self.customer_display_history(key , val)
                elif customer_menu2 ==5 :
                    self.customer_change_pass(key)
                elif customer_menu2 == 6:
                    self.auto_reserve(key , val)
                elif customer_menu2 ==7 :
                    break
    def manager_login(self):
        pass
    def manager_create_room(self):
        # این برعکس داره درست و غلط میگه درستش کن 
        room_code = int(input('enter room number to creat:'))
        room_number = room_code %10 
        bed = (room_code//10 ) %10
        floor = room_code //100 
        # print(f'{room_number} , {bed} , {floor}')
        x=self.logic.manager_create_room(floor , bed , room_number , room_code)
        if x :
            print(x)
            print('ok')

        else :
            print('no')
        
    def manager_display_all_room(self):
        self.logic.manager_display_all_room()

    def manager_display_all_customer(self):
        print(self.logic.manager_display_all_customer())
    def customer_search_with_floors(self):
        rangs_input = input('input range floors you want :(like 1,3)')
        s = self.logic.customer_search_with_floors(rangs_input)

    def manager_display_in_floor(self):
        display_input = int(input('input floor to display all room in floor:'))
        self.logic.anager_display_in_floor(display_input)

    def manager_search_with_room_code(self):
        room_code = int(input('enter room code :'))
        x=self.logic.manager_search_with_room_code(room_code)
        if x:
            print(x)
        else:
            print('not found !!!')   

    def manager_not_active_room(self):
        x = self.logic.manager_not_active_room()
        print(x)

    def manager_change_status_room(self):
        while True:
            change_input = int(input('''___choice to change____
                                     1.change active 
                                     2.change not active'''))
            if change_input == 1:
                new_status = True
                room_code = int(input('input room code to status active'))
                x = self.logic.manager_change_status_room(room_code,new_status)
                if x :
                    print('seccseful .')
                else:
                    print('not seccseful')
                break
            if change_input == 2:
                room_code = int(input('input room code to status active'))
                new_status = False
                x = self.logic.manager_change_status_room(room_code , new_status)
                print('seccesful.')
                break
    def display_history_room(self):
        room_code = int(input('enter room code to display history:'))
        x=self.logic.display_history_room(room_code)
        print(x) 

    def display_reserve_baze(self):
        # start_baze =  input('enter start baze to display:')
        time = Time_l()
        start_year = int(input ('enter start year baze :'))
        start_month = int(input('enter start month baze'))
        start_day = int(input('enter start day baze:'))
        start_baze = time.access(start_year , start_month , start_day)
        # end_baze = input ('enter end baze to display:')
        end_year = int(input('enter end year baze:'))
        end_month = int(input('enter end month baze:'))
        end_day = int(input('enter end day baze:'))
        end_baze = time.access(end_year , end_month , end_day)
        self.logic.display_reserve_baze(start_baze , end_baze)

    def manager_display_canseled(self):
        while True :
            menu  = int(input( '''
                which one you want to see 
                1.change plan 
                2.change place 
                3. other cases


        '''))
            if menu == 1:
                x = 1
                self.logic.display_canseld(x)
                break

            elif menu == 2:
                x = 2
                self.logic.display_canseld(x)
                break

            elif menu == 3 :
                x = 3
                self.logic.display_canseld(x)
                break
    def display_manager_block(self):
        self.logic.display_manager_block()
        while True:
            menu = int(input('''which one
                             1.unblock customer 
                             2.exit
                              '''))
            if menu == 1:
                self.unblock()
                break
            elif menu == 2:
                break

    def unblock(self):
        key = int(input('enter username to unblock'))
        x=self.logic.unblock(key)
        if x:
            print('secsesful')
        else:
            print('cant')
    #  costomer 
        
    def customer_display(self):
        self.logic.customer_display()
    def customer_book_room(self , key , val):
        self.customer_display()
        time = Time_l()
        room_code  = int(input('Please enter the desired room number for reservation :'))
        start_year =  int(input('enter year for resrvaiton start:'))
        start_month = int(input('enter month for resrvaiton start'))
        start_day = int(input('enter day resrvaiton start'))
        start_time = time.access(start_year  , start_month , start_day)
        end_year = int(input('enter year to reservtion end :'))
        end_month = int(input('enter month resrvaiton end'))
        end_day = int(input('enter day resrvaiton end'))
        end_time = time.access(end_year , end_month , end_day)
        code =f'{random.randint(0 , 999999) : 06}'

        x= self.logic.customer_book_room(room_code , start_time , end_time , key , val , code)
        if x:
            print(f' your register code is this : {code}')
    # داخل اون یکی ساختمان داده هم باید  درست کنی 
    def cansel_reserve(self , key , val ):
        register = input('enter register code to cansel reserve')
        while True : 
            menu = int(input('''why do you want to cansel
                             1.change my plan
                             2.change place
                             3.other cases
                              '''))
            if menu == 1:
                x = 'change plan'
                return self.cansel ( register,x ,key , val)
            elif menu == 2:
                x = 'change place'
                return self.cansel( register, x , key , val)
            elif menu == 3:
                x = 'other cases'
                return self.cansel( register,x , key , val)

    def cansel(self , register,x , key ,val ):
        y=self.logic.cansel( register,x , key , val)
        if y:
            print('cansel seccsesful.')

    def customer_display_history(self , key , val):
        x=self.logic.customer_history(key , val)
        print(x)

    def customer_change_pass(self , key ):
        ne_pass = input('enter new pass :')
        x=self.logic.change_pass(key , ne_pass)
        if x:
            print('seccseful.')

        else:
            print('no')

    def auto_reserve(self , key , val):
        bed = int(input('enter how many bed you want :'))
        start_year =  int(input('enter year for resrvaiton start:'))
        start_month = int(input('enter month for resrvaiton start'))
        start_day = int(input('enter day resrvaiton start'))
        start_time = self.time.access(start_year  , start_month , start_day)
        end_year = int(input('enter year to reservtion end :'))
        end_month = int(input('enter month resrvaiton end'))
        end_day = int(input('enter day resrvaiton end'))
        end_time = self.time.access(end_year , end_month , end_day)
        code =f'{random.randint(0 , 999999) : 06}'
        x=self.logic.auto_reserve(key ,bed , start_time , end_time , code , val)
        if x :
             print(f' your register code is this : {code}')
        
    def run(self):
        self.menu()
    