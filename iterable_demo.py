records = [
    ('foo' , 1 , 2),
    ('bar' , 'hello'),
    ('foo' , 3, 4),
    ('f')
]

items = [1,2,3,4,5,6,7,8,9]

def do_foo(x, y):
    print('foo' , x , y)

def do_bar(s):
    print('bar' , s)
    
def sum(items):
    head , *tail = items
    return head + sum(tail) if tail else head

def main():
    for tag , *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)
            
    
    sum(items)
    print(sum(items))
        
        
if __name__ == "__main__":
    main()