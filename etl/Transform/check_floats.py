def convert_floats_cols(test_file, float_cols):
#   loop through each dictionary ROW in the 'test_file' list of dictionaries
    for d in test_file:
        # loop through each KEY with the name 'total_price' and TRY to set it to a float data type
        for col in float_cols:
            # try to convert the value at that key to FLOAT
            try:
                d[col] = float(d[col])
        # if there is a ValueError, set the value to None
            except ValueError:
                d[col] = None
#     return the updated list of dictionaries
    return test_file