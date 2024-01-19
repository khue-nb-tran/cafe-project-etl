import csv
from csv import DictReader

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

def save_data():     #Function to save data to CSV file

     #Save data to products.csv file     
     with open('../data/products.csv', mode='w', newline='') as product_file:
          product_writer = csv.DictWriter(product_file,fieldnames=['Product',' Price'],delimiter=';')
          product_writer.writeheader()
          product_writer.writerows(products_list)

     #Save data to couriers.csv file
     with open('../data/couriers.csv', mode='w', newline='') as courier_file:
          courier_writer = csv.DictWriter(courier_file,fieldnames=['Name',' Phone_Number'], delimiter=';')
          courier_writer.writeheader()
          courier_writer.writerows(couriers_list)

     #Save data to orders.csv file
     with open ('../data/orders.csv', mode='w',newline='') as order_file:
          headings = ['Customer_name',' Customer_address', ' Customer_phone', ' Courier_index',' Products_index',' Status']
          order_writer = csv.DictWriter(order_file, fieldnames=headings,delimiter=';')
          order_writer.writeheader()
          order_writer.writerows(orders_list)

def clear_screen(wait_time):    #Function to clear screen
    import os 
    from time import sleep 

    sleep(wait_time)
    os.system("cls" if os.name == "nt" else "clear")

def display_products():         #Function to display list of products
    print('List of Products:')
    for i, product_item in enumerate(products_list):
        print(f'{i+1}:{product_item['Product']} - Price: {product_item[' Price']}')

def display_couriers():         #Function to display list of couriers
    print('List of Couriers:')
    for i, courier in enumerate(couriers_list):
        print(f'{i+1}:{courier['Name']} - Courier Phone number: {courier[' Phone_Number']}') 

def display_orders ():          #Function to display orders list
    print('List of orders:')
    for i, order in enumerate(orders_list):
        print(f'Order {i+1}: Customer: {order['Customer_name']} - Address: {order[' Customer_address']} - Customer Phone number: {order[' Customer_phone']} - Courier index: {order[' Courier_index']} - Product index: {order[' Products_index']} - Status: {order[' Status']}')
