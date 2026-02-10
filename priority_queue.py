# A sequence of dictionaries or instances and you want to iterate over the data
# in groups based on the value of a particular field, such as date.
from operator import itemgetter
from itertools import groupby

data = [
    {'ip': '192.168.1.1', 'date': '07/01/2012'},
    {'ip': '192.168.1.2', 'date': '07/04/2012'},
    {'ip': '192.168.1.3', 'date': '07/02/2012'},
    {'ip': '192.168.1.4', 'date': '07/03/2012'},
    {'ip': '192.168.1.5', 'date': '07/02/2012'},
    {'ip': '192.168.1.6', 'date': '07/02/2012'},
    {'ip': '192.168.1.7', 'date': '07/01/2012'},
    {'ip': '192.168.1.8', 'date': '07/04/2012'},
]

# sort the list by date
data.sort(key=itemgetter('date'))

# iterate in groups
for date , items in groupby(data , key=itemgetter('date')):
    print('DATE :',date)
    for it in items:
        print(' ' , it)
