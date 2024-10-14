


from node import Node


class AVLTree:
    def __init__(self, comparator):
        self.root = None
        self.comparator = comparator  # comparator is a function that compares two values

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        # Perform rotation
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        # Update heights
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, z):
        # Perform rotation
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        # Update heights
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, value):
        self.root = self._insert(self.root, value)
        

    def _insert(self, node, value):
        if not node:
            return Node(value)

        # Use the comparator to decide where to insert the value
        if self.comparator(value, node.value) < 0:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # Update height of the node
        self.update_height(node)

        # Get the balance factor
        balance = self.get_balance(node)

        # Balance the node if it has become unbalanced
        if balance > 1:  # Left heavy
            if self.comparator(value, node.left.value) < 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        if balance < -1:  # Right heavy
            if self.comparator(value, node.right.value) > 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node or self.comparator(value, node.value) == 0:
            return node
        if self.comparator(value, node.value) < 0:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if not node:
            return node

        if self.comparator(value, node.value) < 0:
            node.left = self._remove(node.left, value)
        elif self.comparator(value, node.value) > 0:
            node.right = self._remove(node.right, value)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._remove(node.right, temp.value)

        # Update height of the current node
        self.update_height(node)

        # Balance the node if it has become unbalanced
        balance = self.get_balance(node)

        # Balance the tree
        if balance > 1:  # Left heavy
            if self.get_balance(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:  # Right heavy
            if self.get_balance(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def find_lfa_gid(self, size):
       
        
        return self._find_lfa_gid(self.root, size)

    def _find_lfa_gid(self, node, size):
        if not node:
            return None
        
        temp = node
       
        while(temp.right!=None):
            temp = temp.right
        
        if(temp.value.capacity<size):
            return None
        else:
            return temp
       
        
    
    def find_lfa_lid(self,size):
        return self._find_lfa_lid(self.root,size)
    def _find_lfa_lid(self,node,size):
        if not node:
            return None
        
        temp = node
        while(temp.right!=None):
            temp = temp.right
        
        a = temp.value.capacity
        
        temp2 = node
        temp3 = None
        while(temp2):
            if(temp2.value.capacity==a):
                temp3 = temp2
                while(temp2.left and temp2.left.value.capacity == a):
                    temp2 = temp2.left
                    temp3 = temp2
                temp2 = temp2.left
            elif(temp2.value.capacity<a):
                temp2 = temp2.right
            elif(temp2.value.capacity>a):
                temp2 = temp2.left
        if(temp3==None):
            return None
        elif(temp3.value.capacity<size):
            return None
        else:
            return temp3
        


    def find_cfa_lid(self,size):
        return self._find_cfa_lid(self.root,size)
    def _find_cfa_lid(self,node,size):
        
        temp = node
        temp2 = None
        while(temp):
            a= temp.value.capacity
            if(a==size):
                temp2 = temp
                temp= temp.left
            
            elif(a>size):
                temp2 = temp
                temp = temp.left
               
            elif(a<size):
                temp = temp.right
       
        return temp2
        
        
        
            
        
    def find_cfa_gid(self,size):
        return self._find_cfa_gid(self.root,size)
    def _find_cfa_gid(self,node,size):
        
        temp = node
        temp2 = None
       
        while(temp):
            a= temp.value.capacity
            if(a==size):
                temp2 = temp
                temp= temp.left
            
            elif(a>size):
                temp2 = temp
                temp = temp.left
                
            elif(a<size):
                temp = temp.right
        if(temp2==None):
            return None
        optimal_capacity = temp2.value.capacity
        temp2 = node
        temp3 = None
        while(temp2):
            if(temp2.value.capacity==optimal_capacity):
                temp3 = temp2
                while(temp2.right and temp2.right.value.capacity == optimal_capacity):
                    temp2 = temp2.right
                    temp3 = temp2
                temp2 = temp2.right
            elif(temp2.value.capacity<optimal_capacity):
                temp2 = temp2.right
            elif(temp2.value.capacity>optimal_capacity):
                temp2 = temp2.left
        if(temp3==None):
            return None
        elif(temp3.value.capacity<size):
            return None
        else:
            return temp3
        
        


    
    def inorder_traversal(self):
        result = []
        nod = self.root
        self._inorder_helper(nod, result)
        return result

    # Helper function for recursion
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)  # Traverse left subtree
            result.append(node.value.object_id)                # Visit node
            self._inorder_helper(node.right, result) # Traverse right subtree