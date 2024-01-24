import csv
from dateutil import parser
from datetime import datetime

#Ensure date in one format
def format_date (dict_list, date_cols):

    for dict in dict_list:
        for col in date_cols:
            try:
                date_object = parser.parse(dict[col], dayfirst=True)
                formatted_date = datetime.strftime(date_object,'%d/%m/%Y %I:%M %p') 
                dict[col] = formatted_date
            except ValueError as e:
                print(f"Error parsing value '{dict[col]}' in column '{col}': {e}")
                dict[col] = None

    return dict_list
