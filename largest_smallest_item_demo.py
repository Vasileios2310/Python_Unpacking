# The heapq module has two functions—nlargest() and nsmallest()
import heapq

nums = [1,2,3,4,5,6,7,-1]

print(heapq.nlargest(3 , nums)) # the three largest numbers in nums
print(heapq.nsmallest(3, nums)) # the three smallest numbers in nums

values = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'APPLE', 'shares': 50, 'price': 543.22},
    {'name': 'SAMSUNG', 'shares': 200, 'price': 21.09},
    {'name': 'XIAOMI', 'shares': 35, 'price': 31.75},
    {'name': '1+', 'shares': 45, 'price': 16.35}
]

print(heapq.nlargest(3 , values , key=lambda s: s ['price']))
print(heapq.nsmallest(3 , values , key=lambda s : s['price'] ))