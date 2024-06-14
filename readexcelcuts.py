import pandas as pd
import re
from collections import defaultdict
global stud_2x4_counts_fromexcelv6
global stud_2x6_counts_fromexcelv6
stud_2x4_counts_fromexcelv6 = {}
stud_2x6_counts_fromexcelv6 = {}
def extract_thisnumbers(sheet_data):
    # Use a regular expression to find all occurrences of "thisnumber" in the format serialnumber(thisnumber)
    pattern = r'\((\d+\.\d+)\)'
    
    thisnumber_counts = defaultdict(int)
    
    # Iterate through each cell in column B
    for cell in sheet_data['Combinations - Serial Number (LF actual inches)']:
        if pd.notna(cell):  # Ensure the cell is not NaN
            matches = re.findall(pattern, str(cell))
            for match in matches:
                # Remove parentheses and convert to integer
                thisnumber = float(match)
                thisnumber_counts[thisnumber] += 1
    
    return dict(thisnumber_counts)

def read_excel_file(file_path):
    # Read the Excel file
    xls = pd.ExcelFile(file_path)
    
    # Read the specified sheets into dataframes
    stud_2x4_df = pd.read_excel(xls, 'Stud 2X4 - Cut Details')
    stud_2x6_df = pd.read_excel(xls, 'Stud 2X6 - Cut Details')
    
    # Extract 'thisnumber' counts from each sheet
    stud_2x4_counts_fromexcelv6 = extract_thisnumbers(stud_2x4_df)
    stud_2x6_counts_fromexcelv6 = extract_thisnumbers(stud_2x6_df)
    
    return stud_2x4_counts_fromexcelv6, stud_2x6_counts_fromexcelv6

def print_dict_line_by_line(dictionary, sheet_name):
    print(f"Dictionary for sheet {sheet_name}:")
    for key, value in sorted(dictionary.items()):
        print(f"{key}: {value}")
    print("\n")

# Example usage
file_path = 'Wastage - v6.xlsx'  # Replace with your file path
stud_2x4_counts_fromexcelv6, stud_2x6_counts_fromexcelv6 = read_excel_file(file_path)

# Print the results
print_dict_line_by_line(stud_2x4_counts_fromexcelv6, 'Stud 2X4 - Cut Details')
print_dict_line_by_line(stud_2x6_counts_fromexcelv6, 'Stud 2X6 - Cut Details')
