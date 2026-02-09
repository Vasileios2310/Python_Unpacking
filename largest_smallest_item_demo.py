# The heapq module has two functions—nlargest() and nsmallest()
import heapq

nums = [1,2,3,4,5,6,7,-1]

print(heapq.nlargest(3 , nums)) # the three largest numbers in nums
print(heapq.nsmallest(3, nums)) # the three smallest numbers in nums