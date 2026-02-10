from collections import namedtuple

Subscriber = namedtuple('Subscriber' , ['addr' , 'joined'])
sub = Subscriber('siberian' , '10-02-2026')
print(sub)

Subscriber(addr = 'siberian' , joined = '10-02-2026')

print(sub.addr)
print(sub.joined)