from functions.data_processor import ExcelDataProcessor, TextDataProcessor

def main():
    # Example usage for .xlsx file
    excel_file_path = 'inputfiles/Wastage - v6.xlsx'  # Replace with your file path
    excel_processor = ExcelDataProcessor()
    stud_2x4_counts, stud_2x6_counts = excel_processor.read_excel_file(excel_file_path)

    def print_dict_line_by_line(dictionary, sheet_name):
        print(f"Dictionary for sheet {sheet_name}:")
        for key, value in sorted(dictionary.items()):
            print(f"{key}: {value}")
        print("\n")

    print_dict_line_by_line(stud_2x4_counts, 'Stud 2X4 - Cut Details')
    print_dict_line_by_line(stud_2x6_counts, 'Stud 2X6 - Cut Details')

    # Example usage for .txt files
    txt_file_path_2x4 = 'inputfiles/Stud_2_4_12_combined.txt'  # Replace with your file path
    txt_processor = TextDataProcessor()
    txt_processor.process_txt_file(txt_file_path_2x4)

    txt_file_path_2x6 = 'inputfiles/Stud_2_6_12_combined.txt'  # Replace with your file path
    txt_processor.process_txt_file(txt_file_path_2x6)

if __name__ == "__main__":
    main()
