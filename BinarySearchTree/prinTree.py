class TreeNode:
    def __init__(self, data):
        # Initialize a node with the given data and set its parent and children
        self.data = data
        self.children = []  # List to hold child nodes
        self.parent = None  # Parent node

    def add_child(self, child):
        # Add a child node to the current node
        child.parent = self  # Set the parent of the child node
        self.children.append(child)  # Add the child to the children list

    def get_level(self):
        # Calculate the level (depth) of the current node in the tree
        level = 0
        p = self.parent  # Start with the parent of the current node
        while p:
            level += 1  # Increment the level for each ancestor
            p = p.parent  # Move to the next ancestor
        return level

    def print_tree(self, level):
        # Print the tree up to a certain level of depth
        spaces = " " * self.get_level() * 3  # Create indentation based on the node's level
        prefix = spaces + "|__" if self.parent else ""  # Add a prefix for child nodes
        
        # Print the current node's data with its level prefix
        print(f"{prefix} {self.data}")
        
        if self.children:
            # Recursively print children if the current level is less than the given level
            for child in self.children:
                if self.get_level() < level:
                    child.print_tree(level)

def build_ManagementHierarchy():
    # Build a hierarchical tree structure representing a management hierarchy
    root = TreeNode("Global")  # Root node of the hierarchy
    
    # Create nodes for different regions and subregions
    India = TreeNode("India")
    Gujarat = TreeNode("Gujarat")
    Ahmedabad = TreeNode("Ahmedabad")
    Baroda = TreeNode("Baroda")
    Karnataka = TreeNode("Karnataka")
    Bangluru = TreeNode("Bangluru")
    Mysore = TreeNode("Mysore")
    USA = TreeNode("USA")
    New_Jersey = TreeNode("New Jersey")
    Princeton = TreeNode("Princeton")
    Trenton = TreeNode("Trenton")
    California = TreeNode("California")
    San_Francisco = TreeNode("San Francisco")
    Mountain_View = TreeNode("Mountain_View")
    Palo_Alto = TreeNode("Palo Alto")
    
    # Build the hierarchy by connecting nodes
    root.add_child(India)
    root.add_child(USA)
    
    India.add_child(Gujarat)
    India.add_child(Karnataka)
    
    Gujarat.add_child(Ahmedabad)
    Gujarat.add_child(Baroda)
    
    Karnataka.add_child(Bangluru)
    Karnataka.add_child(Mysore)
    
    USA.add_child(New_Jersey)
    USA.add_child(California)
    
    New_Jersey.add_child(Princeton)
    New_Jersey.add_child(Trenton)
    
    California.add_child(San_Francisco)
    California.add_child(Mountain_View)
    California.add_child(Palo_Alto)
    
    # Print levels for specific nodes to verify the structure
    print("India Level:", India.get_level())
    print("Root Level:", root.get_level())
    print("Karnataka Level:", Karnataka.get_level())

    return root  # Return the root of the hierarchy

if __name__ == '__main__':
    # Build the tree and print it up to a specified depth level
    root = build_ManagementHierarchy()
    root.print_tree(2)  # Print the tree structure up to level 2
