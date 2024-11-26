import pandas as pd  

def compress(chars):
    write = 0  # Pointer to write in chars
    read = 0   # Pointer to read through chars
    
    while read < len(chars):
        char = chars[read]  # Current character
        count = 0           # Count occurrences of the character
        
        # Count the number of consecutive characters
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        
        # Write the character to the array
        chars[write] = char
        write += 1
        
        # If the count > 1, write the count as well
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    
    return chars[:write]

# Example usage 1 ! 
chars = ["a", "a", "b", "b", "c", "c", "c"]
compressed_length = compress(chars)
print(compressed_length)
# print(chars[:compressed_length])


# Example usage 2 !
chars_2 = ["a"]
compressed_length_2 = compress(chars_2)
print(compressed_length_2)
# print(chars_2[:compressed_length_2])
