import csv
from csv import DictReader
import functions

products_list = []
couriers_list = []
orders_list = []
order_status = []
     
#Read products.csv file into products_list
try: 
     with open('../data/products.csv','r') as product_data:
          product_dict_reader = DictReader(product_data, delimiter=';')
          products_list = list(product_dict_reader) 
except FileNotFoundError:
          print('Products file not found. Starting with an empty products list.')

#Read couriers.csv file into courier_list
try: 
     with open('../data/couriers.csv','r') as courier_data:
          courier_dict_reader = DictReader(courier_data, delimiter=';')
          couriers_list = list(courier_dict_reader)
except FileNotFoundError:
     print('Couriers file not found. Starting with an empty couriers list.')

#Read orders.csv file into orders_list
try:
     with open ('../data/orders.csv','r') as order_data:
          order_dict_reader = DictReader(order_data, delimiter=';' )
          orders_list = list(order_dict_reader)
except FileNotFoundError:
     print('Orders list file not found. Starting with an empty orders list.')

#Main application 

while True: 
    
    #Display main menu options
    print("Main menu options:")
    print('Choose 0 to Exit Main Menu')
    print('Choose 1 to Open Product Menu')
    print('Choose 2 to Open Courier Menu')
    print('Choose 3 to Open Order Menu')

    user_input = int(input('Please choose an option:'))      #Request user input for main menu option
    
    functions.clear_screen(1)

    if user_input == 0: 
        functions.save_data()     #Save data to CSV files

        print('Exiting the app')

        break           #Exit app
    
    elif user_input == 1:

          while True:
               #Display Product menu option
               print('Product Menu Option:')
               print('Choose 0 to Return to Main Menu')
               print('Choose 1 to View Product List')
               print('Choose 2 to Add New Product')

               product_input = int(input('Please choose an option:'))   #Request user input for Product menu option

               functions.clear_screen(1)

               if product_input == 0:
                    print('Returning to Main Menu')
                    break         #Return to main menu

               if product_input == 1:  

                    functions.display_products()

                    functions.clear_screen(6)

               elif product_input == 2:

                    new_product_name = str(input('New product name:'))      #Request user input for new product name
                    new_product_price = float(input('New product price:'))  #Request user input for new product price
                    new_product = {
                         'Product':new_product_name,
                         ' Price':new_product_price
                         }
                    products_list.append(new_product)               #Add new product to product list
                    
                    functions.display_products()
                    functions.clear_screen(5)
                    
               else:
                    print('Please choose a valid option')
    
    elif user_input == 2:

        while True:
            #Display Courier menu option
            print('Courier Menu Option:')
            print('Choose 0 to Return to Main Menu')
            print('Choose 1 to View Courier List')
            print('Choose 2 to Add New Courier')

            courier_input = int(input('Please choose an option:'))   #Request user input for Courier menu option

            functions.clear_screen(1)

            if courier_input == 0:

                print('Returning to Main Menu')

                break         #Return to main menu
            
            if courier_input == 1:  

                functions.display_couriers()

                functions.clear_screen(6)

            elif courier_input == 2:
                
                new_courier_name = str(input('New courier name:'))              #Request user input for new courier name
                new_courier_number = str(input('New courier phone number:'))    #Request user input for new courier name
                
                new_courier = {
                     'Name': new_courier_name,
                     ' Phone_Number': new_courier_number
                }
                
                couriers_list.append(new_courier)                               #Add new courier to courier list
                print(f'{new_courier} has been added to Courier list')

                functions.clear_screen(3)

    elif user_input == 3:
       
        while True:
               print('Choose 0 to Return to Main Menu')
               print('Choose 1 to View Existing Order')
               print('Choose 2 to Create New Order')
               print('Choose 3 to Update Order Status')

               order_input = int(input('Please choose an option:'))

               functions.clear_screen(1)
               
               if order_input == 0:

                    print('Returning to Main Menu')

                    break       #Return to Main Menu

               elif order_input == 1:
                    
                    functions.display_orders()

                    functions.clear_screen(6)
               
               elif order_input == 2:
                
                    customer_name = str(input('Please add customer name:'))
                    customer_address = str(input('Please add customer address:'))
                    customer_phone = str(input('Please add customer phone number:'))

                    #Display Product list with index value
                    functions.display_products()

                    product_indices = str(input('Enter comma-separated product indices (e.g: 0,1,2) to select products: '))

                    #Display Courier list with index value
                    functions.display_couriers()

                    courier_index = int(input('Please input the index of the courier to select:'))

                    new_order = {
                         'Customer_name': customer_name,
                         ' Customer_address': customer_address,
                         ' Customer_phone': customer_phone,
                         ' Courier_index': courier_index,
                         ' Products_index': product_indices,
                         ' Status': 'Preparing'
                    }

                    orders_list.append(new_order)

                    print(f'New order: {new_order} created successfully.' )

                    functions.clear_screen(5)

               elif order_input == 3:
                  
                    #Display order list with index values
                    functions.display_orders()

                    update_order_index = int(input('Please choose order index to update status:')) 

                    print('Status option:')
                    for i, status in enumerate(order_status):
                         print(f'{i+1}:{status}')              #Display order status list with index values

                    status_index = int(input('Please enter the index of the status you want to update'))

                    orders_list[update_order_index - 1][' Status'] = order_status[status_index - 1]   #Updating new value to the "Status" key

                    print('Order status updated successfully.')

                    functions.clear_screen(4)