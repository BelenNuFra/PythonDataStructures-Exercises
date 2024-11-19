"""
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Inicializamos max_product, min_product y res con el primer número de la lista
        max_product = min_product = res = nums[0]

        # Recorremos los números de la lista a partir del segundo elemento
        for i in range(1, len(nums)):
            # Si el número actual es negativo, intercambiamos max_product y min_product
            # porque multiplicar un número negativo por el valor más bajo puede dar el valor más alto
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Actualizamos max_product como el máximo entre el número actual o el producto
            # del número actual con el max_product previo
            max_product = max(nums[i], max_product * nums[i])
            
            # Actualizamos min_product como el mínimo entre el número actual o el producto
            # del número actual con el min_product previo
            min_product = min(nums[i], min_product * nums[i])

            # Actualizamos el resultado con el máximo producto encontrado hasta ahora
            res = max(res, max_product)

        # Retornamos el valor máximo del producto
        return res
