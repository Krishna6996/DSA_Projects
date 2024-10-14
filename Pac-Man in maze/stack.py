class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
      
    # You can implement this class however you like
        self.arr = []
    def push(self,x):
        self.arr.append(x)
    def is_empty(self):
        return len(self.arr)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        else:
            return self.arr.pop()
    def top(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        else:
            return self.arr[-1]
    def to_list(self):
        return self.arr[:]
    