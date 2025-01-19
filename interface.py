import random
class Interface:
    def __init__(self,logic):
        self.logic = logic
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
            9. exit
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
            elif manager_menu == 9 :
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
            self.customer_log(self,key , val)
        else:
            print('no')

    def customer_log(self , key , val):
         while True:

                customer_menu2 = int(input(''' 
                    __customer menu __
                    1.display all room in floor
                    2.book room
                    3.exit
                '''))

                if customer_menu2 == 1:
                    self.customer_display_in_floor()

                if customer_menu2 == 2:
                    self.customer_book_room(key , val)

                if customer_menu2 ==3 :
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
        x=self.logic.manager_create_room(floor , bed , room_number)
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

    #  costomer 
        
    def customer_display(self):
        self.logic.customer_display()
    def customer_book_room(self , key , val):
        self.customer_display()
        room_code  = int(input('Please enter the desired room number for reservation :'))
        start_Time =  input('enter time for resrvaiton start:')
        end_time = input('enter time to reservtion end :')
        self.logic.customer_book_room(room_code , start_Time , end_time , key , val)
        
    def run(self):
        self.menu()
    