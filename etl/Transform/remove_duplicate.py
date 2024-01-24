def remove_duplicate(filename):
    i = 0 
    while i < len(filename):
        dict1 = filename[i]
        j = i + 1

        while j < len(filename):
            dict2 = filename[j]
            
            if sorted(dict1.items()) == sorted(dict2.items()):
               filename.pop(j)

            else: j += 1

        i += 1

    return filename
