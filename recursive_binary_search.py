def recursive_binary_search(number_to_find, numbers, left_number, right_number, list_of_indexes=None): 
    """
    Recursive binary search to find all occurrences of `number_to_find` in the sorted list `numbers`.
    It returns a list of all indexes where the number is found.

    Args:
    number_to_find: The number we are searching for.
    numbers: A sorted list of numbers where we are searching.
    left_number: The left boundary of the search range.
    right_number: The right boundary of the search range.
    list_of_indexes: A list to store the indexes of found elements (default is None).

    Returns:
    list_of_indexes: A list of indexes where the number is found.
    """
    
    length = len(numbers)  # Get the length of the list
    mid_index = (left_number + right_number) // 2  # Calculate the middle index of the current range
    mid_number = numbers[mid_index]  # Get the number at the middle index
    
    # Initialize the list_of_indexes if it's the first recursive call
    if list_of_indexes is None:
        list_of_indexes = []

    # Base case: if the search range is invalid, stop the recursion
    if left_number > right_number:
        return list_of_indexes
    
    # If mid_index is out of range (shouldn't happen in a valid call), return -1
    if mid_index >= len(numbers): 
        return -1 
    
    # If the number_to_find is less than the mid_number, search in the left half
    if number_to_find < mid_number: 
        return recursive_binary_search(number_to_find, numbers, left_number, mid_index - 1, list_of_indexes)
        
    # If the number_to_find is greater than the mid_number, search in the right half
    if number_to_find > mid_number: 
        return recursive_binary_search(number_to_find, numbers, mid_index + 1, right_number, list_of_indexes)
        
    # If the mid_number matches the number_to_find, we found an occurrence
    if mid_number == number_to_find:
        list_of_indexes.append(mid_index)  # Add the current index to the list of indexes

        # Search to the left and right of the current mid_index to find all occurrences
        list_of_indexes = recursive_binary_search(number_to_find, numbers, left_number, mid_index - 1, list_of_indexes)
        list_of_indexes = recursive_binary_search(number_to_find, numbers, mid_index + 1, right_number, list_of_indexes)
    
    return list_of_indexes

# Main function to test the recursive binary search
if __name__ == '__main__': 
    # Example list with duplicate values
    numbers_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    
    # Search for the number 15 in the list
    index = recursive_binary_search(15, numbers_list, 0, len(numbers_list)-1)
    
    # Print the list of indexes where 15 is found
    print(index)
