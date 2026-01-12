# Unpacking a Sequence into Separate Variables.
# Any sequence (or iterable) can be unpacked into variables using a simple assignment
# operation. The only requirement is that the number of variables and structure match the sequence.
# Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators.

p = (1,4)
x , z = p
print(x)
print(z)

print('------------------------------')

data = ['Apple' , 'Banana' , 'Carrot' ]
fruit1 , fruit2 , fruit3 = data
print(fruit1)
print(fruit2)
print(fruit3)

print('------------------------------')
data = ['siberian' , 35 , 'software developer', 'basketball' , (12 , 1 , 2026)]
username , age , job , sport , (day , month , year) = data
print(username)
print(age)
print(job)
print(sport)
print(day)
print(month)
print(year)
print('------------------------------')
s= 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(c)
print(d)
print(e)

print('------------------------------')
data2 = [ 'siberian', 100, 1.1, (2026, 5, 2) ]
_, shares, price, _ = data2
print(shares) 