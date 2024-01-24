clean_data_list = []

def clean_empty_data(filename):            
    for row in filename:
        if '' not in row.values():
            clean_data_list.append(row)
    return clean_data_list