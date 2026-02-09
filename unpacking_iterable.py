records = ('Dave' , 'dave@example.com' , '123-456789' , 'Mathematics')

name , email , phone_number , department = records

print(name)
print(email)
print(phone_number)
print(department)

print('-' *40)
# The starred variable can also be the first one in the list
*trailing , current = [10,8,7,9,6,5,4,3]
print(f"trailing --> ",trailing)
print(f"current --> ",current)

print('-' *40)
# Sometimes you might want to unpack values and throw them away. You can’t just specify
# a bare * when unpacking, but you could use a common throwaway variable name, such
# as _ or ign (ignored). 

record = ('NBA' , 50 , 3.14 , (12 , 2 ,  2022))
name , *_ , (*_, year) = record

print(name)
print(year)

print('-' *40)
# There is a certain similarity between star unpacking and list-processing features of var
# ious functional languages. For example, if you have a list, you can easily split it into head
# and tail components like this:
items = [1,2,3,4,5,6,7,8,9]
head , *tail = items
*head2 , tail2 = items
print(f"Head of items : " , head)
print(f"Tail of items : " , tail)
print(f"First items : " , *head2)
print(f"Last item : " , tail2)