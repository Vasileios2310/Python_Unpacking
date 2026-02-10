from collections import deque

def search (lines , pattern , history = 5):
    """Following code performs a simple text match on a sequence of lines and yields the
        matching line along with the previous N lines of context when found
        
    """
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line , previous_line
        previous_line.append(line)
        
if __name__ == "__main__":
    with open('file.txt') as f:
        for line , prevlines in search(f , 'python' , 5):
            for pline in prevlines:
                print(line , end='')
            print(line , end ='')