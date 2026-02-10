from collections import namedtuple

Stock = namedtuple('Stock' , ['name' , 'shares' , 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total 

records = [
    ('IBM', 100, 91.1),
    ('AAPL', 50, 175.2),
]

print(compute_cost(records))  # 100*91.1 + 50*175.2
