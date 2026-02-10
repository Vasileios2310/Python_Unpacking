from itertools import compress
""" takes an iterable and
    an accompanying Boolean selector sequence as input. As output, it gives you all of the
    items in the iterable where the corresponding element in the selector is True. This can
    be useful if you’re trying to apply the results of filtering one sequence to another related
    sequence
"""
data = [
    '192.168.1.1',
    '192.168.1.2',
    '192.168.1.3',
    '192.168.1.4',
    '192.168.1.5',
    '192.168.1.6',
    '192.168.1.7',
    '192.168.1.8',
]

counts = [0, 3 , 5 , 6 , 7 , 8 , 9 , 4]

# returns True if n > 5, otherwise False
more5 = [n > 5 for n in counts]
print(more5)

#  compress() normally returns an iterator. Thus, you need to use list() to turn the results into a list if desired.
comperssed_list = list(compress(data , more5))
print(comperssed_list)