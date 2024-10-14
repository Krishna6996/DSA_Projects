from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException




def compare_capacity_then_greatest_id(bin_a, bin_b):
    if bin_a.capacity == bin_b.capacity:
        return bin_a.bin_id - bin_b.bin_id
    return bin_a.capacity - bin_b.capacity





class GCMS:
    def __init__(self):
        
        
        self.bins_by_capacity_id = AVLTree(compare_capacity_then_greatest_id)
        self.bins_by_id = AVLTree(lambda a, b: a.bin_id - b.bin_id)
        self.objects_by_id = AVLTree(lambda a, b: a.object_id - b.object_id)

    def add_bin(self, bin_id, capacity):
        temp_bin = Bin(bin_id, capacity)
       
        
        self.bins_by_id.insert(temp_bin)
       
        # Add the bin to the AVL Trees
        self.bins_by_capacity_id.insert(temp_bin)


        # Insert into bin_id AVL tree
        # self.bins_by_id.insert(temp_bin)
        
        

    def add_object(self, object_id, size, color):
        obj = Object(object_id, size, color)
      
        if color == Color.BLUE:
            # Compact Fit Algorithm, Least ID
            
            bin_node = self.find_suitable_bin1(self.bins_by_capacity_id, size)
        elif color == Color.YELLOW:
            # Compact Fit Algorithm, Greatest ID
            bin_node = self.find_suitable_bin2(self.bins_by_capacity_id, size)
        elif color == Color.RED:
            # Largest Fit Algorithm, Least ID
            
            bin_node = self.find_suitable_bin3(self.bins_by_capacity_id, size)
            
        elif color == Color.GREEN:
            # Largest Fit Algorithm, Greatest ID
            bin_node = self.find_suitable_bin4(self.bins_by_capacity_id, size)
            
        else:
            raise NoBinFoundException

        if not bin_node:
            raise NoBinFoundException

        # Add object to the bin and update AVL trees
        bin_node.value.add_object(obj)
        self.update_bin_capacity(bin_node.value, size)
        

        # Add object to object AVL Tree
        self.objects_by_id.insert(obj)
        return True

    def find_suitable_bin1(self, avl_tree, object_size):
        """
        Search for the suitable bin in the AVL tree.
        """
        return avl_tree.find_cfa_lid(object_size)
    
    def find_suitable_bin2(self, avl_tree, object_size):
        return avl_tree.find_cfa_gid(object_size)
    
    def find_suitable_bin3(self, avl_tree, object_size):
        """
        Search for the suitable bin in the AVL tree.
        """
        return avl_tree.find_lfa_lid(object_size)
    
    def find_suitable_bin4(self,avl_tree,object_size):
        
        return avl_tree.find_lfa_gid(object_size)
        
        

    def update_bin_capacity(self, bin, object_size):
        """
        Update the capacity of the bin in all AVL trees.
        """
        # Remove the bin from AVL trees before capacity update
        self.bins_by_capacity_id.remove(bin)
        

        # Update capacity
        bin.capacity -= object_size

        # Re-insert the bin with updated capacity
        self.bins_by_capacity_id.insert(bin)
        

    def delete_object(self, object_id):
        """
        Remove an object from its bin.
        """
        temp_object = Object(object_id,0,0)
        obj_node = self.objects_by_id.search(temp_object)
        if  not obj_node:
           return None

        obj = obj_node.value
        bin_node = self.bins_by_id.search(obj)
        bin_node.value.remove_object(object_id)
        self.objects_by_id.remove(obj)
        # Revert bin's capacity
        self.update_bin_capacity(bin_node.value, -obj.size)

    def object_info(self, object_id):
        """
        Return the bin ID for the given object.
        """
        temp_object = Object(object_id,0,0)
        obj_node = self.objects_by_id.search(temp_object)
        if obj_node:
            return obj_node.value.bin_id
        return None

    def bin_info(self, bin_id):
        """
        Return the current capacity and list of object IDs in the bin.
        """
        temp_bin = Bin(bin_id,0)
        
        
        bin_node = self.bins_by_id.search(temp_bin)
        if bin_node:
            
            bin = bin_node.value
            arr = bin_node.value.objects.inorder_traversal()
            return (bin.remaining_capacity,arr)
        return None  
            
        