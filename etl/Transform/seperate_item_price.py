from csv import DictReader
import csv

def item_price(orders, order_columns):
    for row in orders:
        for col in order_columns:
            if col in row: #check if key exists in dict
                split_items = row[col].split(', ')
                
                double_split_items = [item.split(' - ') for item in split_items]

                item_dicts = []  

                for item in double_split_items:
                    products = {}  
                    try:
                        products.update({
                            "name": item[0],
                            "flavour": item[1],
                            "price": item[2],
                        }) 
                    except IndexError:
                        products.update({
                            "name": item[0],
                            "flavour": None,
                            "price": item[1],
                        }) 
                    item_dicts.append(products)

                row[col] = item_dicts
            else:
                print(f"Key '{col}' not found in dictionary: {row}")
                
    return(orders)
                