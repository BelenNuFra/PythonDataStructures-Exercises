class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
        
    def find_min(self):
        # caso de arbol vacío 
        if self is None:
            return None
        #solo hay un valor 
        if self.right and self.left == None: 
            return self.data
            
        # buscar en el lado izquierdo 
        if self.left: 
            return self.left.find_min()
        else: 
            return self.data
        
    def find_max(self):
        # caso de arbol vacío 
        if self is None:
            return None
            
        # buscar en el lado izquierdo 
        if self.right: 
            return self.right.find_max()
        else: 
            return self.data
            
    def print_tree(self, level=0):
        if self is not None:
            if self.right:  # Verificar si hay un subárbol derecho
                self.right.print_tree(level + 1)
            print(' ' * 4 * level + '-> ' + str(self.data))
            if self.left:  # Verificar si hay un subárbol izquierdo
                self.left.print_tree(level + 1)
                
    def sum(self, sumA = 0):
        if self is None: 
            return 0
        else:
            if self.right:
                sumA = sumA + int(self.right.data)
                self.right(sumA)
            if self.left:
                sumA = sumA + int(self.left.data)
                self.left(sumA)
        return sumA
            


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    numbers_tree.print_tree()
    print("The minimun number in the tree is:",numbers_tree.find_min())
    print("The max number in the tree is:",numbers_tree.find_max())
    print("The sum is:",numbers_tree.sum())
    
    
    
    
    
    