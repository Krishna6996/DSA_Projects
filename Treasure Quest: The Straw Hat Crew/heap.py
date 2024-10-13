

class Heap:
    
    
    def __init__(self, comparison_function, init_array):
        
        self.data= init_array
        self.comparator = comparison_function
        self.build_heap()
        
    def size(self):
        return len(self.data)   
       
    
    def insert(self, value):
       
        self.data.append(value)  
        i = self.size() - 1  
        while i > 0 and  self.comparator(self.data[i], self.data[self.parent(i)]):  
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]  
            i = self.parent(i) 

    def get_min(self):  
        if  self.size()> 0:  
            return self.data[0]  
        else:  
            return None  
        
        
     
    def extract(self):
       
        if self.size()==0:
            return None
        else:
            temp = self.data[0]
            self.data[0],self.data[len(self.data)-1] = self.data[len(self.data)-1],self.data[0]
            self.data.pop()
            self.heapify(0)
            return temp
        
        
        
    
    def top(self):
        
        if self.size() > 0:
            return self.data[0] 
        else:
            return None
       
    
   
    def parent(self, i):  
        return (i - 1) // 2  
    def left_child(self, i):  
        return 2 * i + 1  
    def right_child(self, i):  
        return 2 * i + 2  
    def build_heap(self):
        if(self.size()==0):
            return None
        else:
            for i in range(self.size() // 2 - 1, -1, -1): 
                self.heapify(i)

    def heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size() and self.comparator(self.data[left], self.data[smallest]):
            smallest = left

        if right < self.size() and self.comparator(self.data[right], self.data[smallest]):
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify(smallest)
