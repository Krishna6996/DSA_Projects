from avl import AVLTree
from object import Object
def compare_by_object_id(obj1, obj2):
    return obj1.object_id - obj2.object_id

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.remaining_capacity = capacity
        self.objects = AVLTree(compare_by_object_id)

    def add_object(self, object):
       
        if object.size <= self.remaining_capacity:
            self.objects.insert(object)
            self.remaining_capacity -= object.size
            object.bin_id = self.bin_id  # Assign the bin ID to the object
            return True
        return False #error dena hain


    def remove_object(self, object_id):
         temp_node = Object(object_id,0,0)
         object_node = self.objects.search(temp_node)
         if object_node:
            obj = object_node.value
            self.remaining_capacity += obj.size  # Restore the bin's capacity
            self.objects.remove(obj)
            return True
         return False
