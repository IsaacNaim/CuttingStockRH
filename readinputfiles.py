def read_decimal_numbers(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split the content based on any whitespace
    numbers_str = content.split()
    
    # Convert the split strings to floats
    numbers = [float(num) for num in numbers_str]
    
    return numbers

def count_numbers(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts

# Example usage
file_path = 'Stud_2_4_12_combined.txt'  # Replace with your file path
numbers = read_decimal_numbers(file_path)
number_counts = count_numbers(numbers)

print(number_counts)
