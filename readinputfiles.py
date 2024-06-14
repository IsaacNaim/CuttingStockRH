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

def sort_counts(counts):
    # Sort the dictionary by keys (the numbers) in ascending order
    sorted_counts = dict(sorted({key + 0.125: value for key, value in counts.items()}.items()))
    return sorted_counts

def sort_counts_old(counts):
    # Sort the dictionary by keys (the numbers) in ascending order
    sorted_counts = dict(sorted(counts.items()))
    return sorted_counts


def print_sorted_counts(sorted_counts):
    for number, count in sorted_counts.items():
        print(f"{number}: {count}")

def multiply_and_sum(sorted_counts):
    total = sum(key * value for key, value in sorted_counts.items())
    return total

# Example usage
file_path = 'Stud_2_4_12_combined.txt'  # Replace with your file path
numbers = read_decimal_numbers(file_path)
number_counts = count_numbers(numbers)
sorted_number_counts_withbladecuts = sort_counts(number_counts)
sorted_number_counts = sort_counts_old(number_counts)
totalwithbladecuts = multiply_and_sum(sorted_number_counts_withbladecuts)
total = multiply_and_sum(sorted_number_counts)
print("Stud_2_4_12_combined.txt file")
print("Sum of all numbers: "+str(round(total,2)))
print("Sum of all numbers minutes with 0.125 inch blade cut: "+str(round(totalwithbladecuts,2)))
print_sorted_counts(sorted_number_counts)
# Example usage
file_path = 'Stud_2_6_12_combined.txt'  # Replace with your file path
numbers = read_decimal_numbers(file_path)
number_counts = count_numbers(numbers)
sorted_number_counts_withbladecuts = sort_counts(number_counts)
sorted_number_counts = sort_counts_old(number_counts)
totalwithbladecuts = multiply_and_sum(sorted_number_counts_withbladecuts)
total = multiply_and_sum(sorted_number_counts)
print("Stud_2_6_12_combined.txt file")
print("Sum of all numbers: "+str(round(total,2)))
print("Sum of all numbers minutes with 0.125 inch blade cut: "+str(round(totalwithbladecuts,2)))
print_sorted_counts(sorted_number_counts)
