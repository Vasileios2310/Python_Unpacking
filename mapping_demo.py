from collections import namedtuple

Stock = namedtuple('Stock' , ['name' , 'shares' , 'price'])

records = [
    ('IBM', 100, 91.1),
    ('AAPL', 50, 175.2),
]

stock_prototype = Stock('' , 0 , 0)


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total 
print(compute_cost(records))  # 100*91.1 + 50*175.2

def dict_to_stock(s):
    return stock_prototype._replace(**s)

stock1 = {'name' : 'APPLE', 'shares' : 100, 'price' : 91.1 }
print(dict_to_stock(stock1))