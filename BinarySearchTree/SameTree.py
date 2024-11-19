"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Si ambos nodos son None, son iguales en esta rama, no hay nada que comparar
        if not p and not q:
            return True
        
        # Si uno de los nodos es None y el otro no, o sus valores no coinciden, los árboles no son iguales
        if not p or not q or p.val != q.val:
            return False
        
        # Llamadas recursivas para comparar los subárboles izquierdo y derecho de ambos árboles
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
