from connect_to_db import *
from generate_sql_db import *
import csv
from io import StringIO
import ast
from datetime import datetime
import uuid


ssm_param_name = 'twomuchsauce_redshift_settings'

def lambda_handler(event, context):
    print('lambda_handler: starting')
    
    s3 = boto3.client('s3')
    print(event)
    # Get the bucket name and key for the uploaded file
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(source_bucket, key)
    
    # Get the file object from S3
    file_obj = s3.get_object(Bucket=source_bucket, Key=key)
    file_content = file_obj['Body'].read().decode('utf-8')
    #transactions = csv.DictReader(StringIO(file_content))
    transactions = list(csv.DictReader(StringIO(file_content)))

    
    for row in transactions:
        row['order'] = ast.literal_eval(row['order'])
        
    connection, cursor = open_sql_database_connection_and_cursor()

    create_db_tables(connection, cursor)

    products = get_product_prices(transactions)  # acutally just unique_produts_list from below
    
    orders = insert_orders(connection, cursor, transactions)
    
    # Call the function to insert products into the database
    products = insert_products_db(connection, cursor, products)
    
    insert_order_breakdown(connection, cursor, transactions, orders, products)
    
    
    cursor.close()
   
    print(transactions)


def insert_products_db(connection, cursor, products):
    print(products)
    # Insert products into the 'products' table
    for product in products:
        # Check if the product already exists
        check_sql = "SELECT product_id FROM products WHERE product_name = %s AND price = %s"
        data_values = (product['name'], product['price'])

        cursor.execute(check_sql, data_values)
        existing_product_id = cursor.fetchone()
        
        if existing_product_id is None:
            product_id = str(uuid.uuid4())
            # If the product doesn't exist, insert it
            insert_sql = """INSERT INTO products (product_id,product_name, price) VALUES (%s, %s,%s)"""
            cursor.execute(insert_sql, (product_id, product['name'], product['price']))
            
            product['product_id'] = product_id
            connection.commit()
            
        else:
            product['product_id'] = existing_product_id
    

    return products            
        
def insert_orders(connection, cursor, orders):
    
    for order in orders:
        # Check if the order already exists

        order_id= str(uuid.uuid4())            
        sql = """INSERT INTO Orders (order_ID, order_date, payment_type, branch) VALUES (%s,%s,%s,%s)"""
        
        # Format the date as needed
        
        date_object = datetime.strptime(order['date'], '%d/%m/%Y %I:%M %p')

        formatted_date = date_object.strftime('%Y-%m-%d %H:%M')
        
        data_values=(order_id, formatted_date, order['payment_type'], order['location'] )
        
        cursor.execute(sql, data_values)

        order['order_id'] = order_id
        connection.commit()
        
    
    # cursor.close()
    
    return orders
    

def insert_order_breakdown(connection, cursor, transactions, orders, products):
    for transaction in transactions:
        order_id = transaction["order_id"]
        for current_product in transaction["order"]:
            product_id = next(product["product_id"] for product in products if product["name"] == current_product["name"])
            quantity = current_product["quantity"]
            flavour = current_product['flavour']
            product_price = next(product["price"] for product in products if product["product_id"] == product_id)
            total_price = quantity * product_price
            sql = """INSERT INTO order_breakdown (order_id, product_id, quantity, flavour, total_price) VALUES (%s, %s, %s, %s, %s)"""
            data = (order_id, product_id, quantity, flavour, total_price)
            cursor.execute(sql, data)
            connection.commit()  
             

def insert_payment_type_db(connection, cursor, payment_types):
    print(payment_types)
    # Insert payment types into the 'payment_type' table
    for i in range(len(payment_types)):
        # Check if the payment_type already exists
        check_sql = "SELECT payment_typeID FROM payment_type WHERE type_name = %s"
        cursor.execute(check_sql, (payment_types[i],))
        existing_type_id = cursor.fetchone()
        
        if existing_type_id == None:
            payment_id= str(uuid.uuid4())
            sql = """INSERT INTO payment_type (payment_typeID,type_name) VALUES (%s,%s)"""
            cursor.execute(sql, (payment_id,payment_types[i]))
            
            last_inserted_id = payment_id
            # changing the payment_types list created above, payment_types=["CASH","CARD"] to a list of 2 dicts as described below
            payment_types[i] = {'payment_type_id': last_inserted_id, 'type_name': payment_types[i]}
            connection.commit()
        else:
            payment_types[i] = {'payment_type_id': existing_type_id, 'type_name': payment_types[i]}
    
    # cursor.close()
    
    return payment_types            
    
def insert_transactions_db(connection, cursor, transactions, branches, payment_types):
    for transaction in transactions:
        # Get branch_id and payment_type_id using the fetched values
        branch_id = next(branch['branch_id'] for branch in branches if branch['branch_name'] == transaction['location'])
        payment_type_id = next(type['payment_type_id'] for type in payment_types if type['type_name'] == transaction['payment_type'])
        total_cost = float(transaction['total'])
    
        # Format the date as needed
        date_object = datetime.strptime(transaction['date'], '%d/%m/%Y %H:%M')
        formatted_date = date_object.strftime('%Y-%m-%d %H:%M')
        
        # Insert transaction data into the 'transactions' table
        sql = """INSERT INTO transactions (orderID,branchID, payment_typeID, total_cost, order_datetime) VALUES (%s,%s, %s, %s, %s)"""
        orderid= str(uuid.uuid4())
        data = (orderid,branch_id, payment_type_id, total_cost, formatted_date)
        cursor.execute(sql, data)
        
        # Fetch the last inserted order_id using IDENT_CURRENT
        #cursor.execute("SELECT IDENT_CURRENT('transactions')")
        #ohh. so we're adding a new key value pair for each record in the csv
        transaction['order_id'] = orderid
        connection.commit()
    print('Committed transactions')
        
    # cursor.close()
    return transactions

def get_product_prices(transactions):
    unique_products_dict = {}

    # Iterate through the data_list and update the unique_products_dict
    for entry in transactions:
        order = entry.get('order', [])
        for product in order:
            product_name = product['name']
            if product_name not in unique_products_dict:
                unique_products_dict[product_name] = {'name': product_name, 'price': product['price']}

    # Convert the values of the unique_products_dict to a list of dictionaries
    unique_products_list = list(unique_products_dict.values())
    print(unique_products_list)
    return unique_products_list

def get_unique_branches(transactions):
    branches = []
    branch_names = []
    for record in transactions:
        if record['location'] not in branch_names:
            branch_names.append(record['location'])
            branches.append({'branch_name': record['location']})
    return branches
    