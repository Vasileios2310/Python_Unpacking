# data inside of a sequence, and need to extract values or reduce the sequence
# using some criteria

values = ['100', '2.4', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

# filter() creates an iterator, so if you want to create a list of results, make sure you also use list() as shown  
invals = list(filter(is_int, values))    
print(invals)