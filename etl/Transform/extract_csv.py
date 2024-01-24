import csv
from csv import DictReader
import time

def read_file(filename):    

    try:
        with open(filename, 'r') as csv_file:
    
            csv_reader = csv.reader(csv_file)

            initial_dictionary = []

            final_dictionary = []

            # Extract each dictionary row/record (within the csv_reader object) to the initial_dictionary list
            for row in csv_reader:
                initial_dictionary.append(row)

            # Create the header column names for each field of the CSV file
            header = ['date','location','name','order','total_price','payment_type','card_no']

            # Loop through the row of dictionary records contained within the initial_dictionary list
            for values in initial_dictionary:
                # Zip column names & values to synchronise KEYS with corresponding VALUES for each dictionary row
                zipped_data = zip(header, values)
                # Convert the zipped KEY-VALUE pairs into dictionary format, & append to final_dictionary list.
                final_dictionary.append(dict(zipped_data))
        
        return final_dictionary
    
    except FileNotFoundError:
        print('Sorry - the filename you entered does not exist!')
        exit()


