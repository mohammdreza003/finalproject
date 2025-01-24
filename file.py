# from logic import Logic
# from customer_node import Customer_node

# class Read_file:
#     def __init__(self):
#         self.logic =  Logic()

#     def user_read(self):
#         with open('test_user.txt', 'r') as users_file:
#             lines = users_file.readlines()  
#             print('p')
#             for line in lines:
#                 line = line.strip()  
#                 key, value = line.split(',')  
#                 print('*')
#                 self.logic.hash_customer.insert(key , Customer_node(key , value))
#                 # self.logic.hash_customer.display()

#     def room_read(self):
#         pass




#     def run(self):

#         self.user_read()

# f = Read_file()
# f.user_read()