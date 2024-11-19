# Class representing a simple HashMap with collision handling using chaining
class HashMap: 
    def __init__(self): 
        # Set a fixed size for the hash table
        self.maxLength = 10 
        # Create an array of empty lists (buckets) for handling collisions
        self.weatherArr = [[] for i in range(self.maxLength)]
    
    def getHash(self, key): 
        """
        Generate a hash value for the given key using a simple algorithm.
        The hash is the sum of ASCII values of characters in the key,
        modulo the maximum length of the array.
        """
        hash = 0
        for char in key: 
            hash += ord(char)  # Sum the ASCII values of all characters in the key
        return hash % self.maxLength  # Ensure the hash is within the bounds of the array
    
    def getItem(self, key): 
        """
        Retrieve the value associated with the given key.
        """
        h = self.getHash(key)  # Get the hash index for the key
        
        # Iterate through the bucket at the hash index to find the key
        for index, element in enumerate(self.weatherArr[h]): 
            if len(element) == 2 and element[0] == key:  # Check if the key exists
                print(f"El valor de {element[0]} es {element[1]}")  # Print the value
    
    def insertItem(self, key, value): 
        """
        Insert a key-value pair into the hash map.
        If the key already exists, update its value.
        """
        h = self.getHash(key)  # Get the hash index for the key
        
        # Check if the key already exists in the bucket
        for idx, (k, _) in enumerate(self.weatherArr[h]):
            if k == key:
                self.weatherArr[h][idx] = (key, value)  # Update the value if key exists
                return
        
        # If the key doesn't exist, append it to the bucket
        self.weatherArr[h].append((key, value))
    
    def __str__(self):
        """
        Provide a string representation of the hash map for easy visualization.
        Only non-empty buckets are included.
        """
        result = "{\n"
        for i, bucket in enumerate(self.weatherArr):
            if bucket:  # Only include buckets with elements
                result += f"  Bucket {i}: "
                result += ", ".join([f"{k}: {v}" for k, v in bucket]) + "\n"
        result += "}"  # Close the dictionary-like representation
        return result

def main():
    # Create a new HashMap object
    hm = HashMap()

    # Insert key-value pairs representing dates and temperatures
    hm.insertItem("Jan 1", 27)
    hm.insertItem("Jan 2", 31)
    hm.insertItem("Jan 3", 23)
    hm.insertItem("Jan 4", 34)
    hm.insertItem("Jan 5", 37)
    hm.insertItem("Jan 6", 38)
    hm.insertItem("Jan 7", 29)
    hm.insertItem("Jan 8", 30)
    hm.insertItem("Jan 9", 35)
    hm.insertItem("Jan 10", 30)
    
    # Calculate and print hash values for specific keys
    h = hm.getHash("Jan 8")
    h = hm.getHash("Jan 9")
    h = hm.getHash("Jan 10")
    
    # Retrieve and print values associated with specific keys
    print(hm)  # Print the entire hash map
    hm.getItem("Jan 9")  # Retrieve value for "Jan 9"
    hm.getItem("Jan 10")  # Retrieve value for "Jan 10"

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
