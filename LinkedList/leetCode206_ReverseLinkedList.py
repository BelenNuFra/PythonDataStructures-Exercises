#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Inicializar el puntero 'prev' a None, para el nuevo final de la lista invertida
        current = head  # Establecer 'current' como el nodo de inicio de la lista
        inverted_list = []  # Inicializar una lista para guardar los valores invertidos (aunque no se usa para la solución)

        while current:  # Mientras haya nodos en la lista
            next_node = current.next  # Guardar el siguiente nodo
            inverted_list.append(current.val)  # Agregar el valor del nodo actual a la lista de valores invertidos
            current.next = prev  # Invertir el enlace: el siguiente nodo de 'current' debe apuntar a 'prev'
            prev = current  # Mover 'prev' un paso adelante, convirtiéndose en el nuevo nodo anterior
            current = next_node  # Mover 'current' un paso adelante, a la siguiente posición en la lista

        self.head = prev  # Al final del ciclo, 'prev' apuntará al nuevo encabezado de la lista invertida
        
        return self.head  # Retornar el nuevo encabezado de la lista invertida
