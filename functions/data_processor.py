import pandas as pd
import re
from collections import defaultdict

class DataProcessor:
    def count_numbers(self, numbers):
        counts = {}
        for number in numbers:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1
        return counts

    def sort_counts(self, counts):
        # Sort the dictionary by keys (the numbers) in ascending order
        sorted_counts = dict(sorted(counts.items()))
        return sorted_counts

    def print_sorted_counts(self, sorted_counts):
        for number, count in sorted_counts.items():
            print(f"{number}: {count}")

    def multiply_and_sum(self, sorted_counts):
        total = sum(key * value for key, value in sorted_counts.items())
        return total

class ExcelDataProcessor(DataProcessor):
    def extract_thisnumbers(self, sheet_data):
        # Normalize column names by stripping whitespace
        sheet_data.columns = sheet_data.columns.str.strip()
        
        # Check if column 'B' exists
        if 'Combinations - Serial Number (LF actual inches)' not in sheet_data.columns:
            print("Column 'Combinations - Serial Number (LF actual inches)' not found in the sheet.")
            return {}
        
        # Use a regular expression to find all occurrences of numbers in parentheses
        pattern = r'\((\d+\.\d+)\)'
        
        thisnumber_counts = defaultdict(int)
        
        # Iterate through each cell in column B
        for cell in sheet_data['Combinations - Serial Number (LF actual inches)']:
            if pd.notna(cell):  # Ensure the cell is not NaN
                matches = re.findall(pattern, str(cell))
                for match in matches:
                    # Convert to float
                    thisnumber = float(match)
                    thisnumber_counts[thisnumber] += 1
        
        return dict(thisnumber_counts)

    def read_excel_file(self, file_path):
        # Read the Excel file
        xls = pd.ExcelFile(file_path)
        
        # Read the specified sheets into dataframes
        stud_2x4_df = pd.read_excel(xls, 'Stud 2X4 - Cut Details')
        stud_2x6_df = pd.read_excel(xls, 'Stud 2X6 - Cut Details')
        
        # Extract 'thisnumber' counts from each sheet
        stud_2x4_counts = self.extract_thisnumbers(stud_2x4_df)
        stud_2x6_counts = self.extract_thisnumbers(stud_2x6_df)
        
        return stud_2x4_counts, stud_2x6_counts

class TextDataProcessor(DataProcessor):
    def read_decimal_numbers(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Split the content based on any whitespace
        numbers_str = content.split()
        
        # Convert the split strings to floats
        numbers = [float(num) for num in numbers_str]
        
        return numbers

    def process_txt_file(self, file_path):
        numbers = self.read_decimal_numbers(file_path)
        number_counts = self.count_numbers(numbers)
        sorted_number_counts = self.sort_counts(number_counts)
        total = self.multiply_and_sum(sorted_number_counts)
        
        print(f"{file_path} file")
        print("Sum of all numbers: " + str(round(total, 2)))
        self.print_sorted_counts(sorted_number_counts)
