from functions.data_processor import ExcelDataProcessor, TextDataProcessor
from functions.dictionary_comparator import DictionaryComparator
from functions.excel_output_generator import generate_excel_output

def main():
  
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

  
    txt_file_path_2x4 = 'inputfiles/Stud_2_4_12_combined.txt'  # Replace with your file path
    txt_processor = TextDataProcessor()
    text_counts_2x4 =  txt_processor.process_txt_file(txt_file_path_2x4)

    txt_file_path_2x6 = 'inputfiles/Stud_2_6_12_combined.txt'  # Replace with your file path
    text_counts_2x6 = txt_processor.process_txt_file(txt_file_path_2x6)

    # Compare dictionaries and visualize
    comparator_2x4 = DictionaryComparator(stud_2x4_counts, text_counts_2x4, "Excel Stud 2X4", "Text Stud 2X4")
    common_keys_2x4, unique_to_dict1_2x4, unique_to_dict2_2x4, common_counts_2x4 = comparator_2x4.compare_dictionaries()
    comparator_2x4.plot_bar_chart(common_counts_2x4)

    comparator_2x6 = DictionaryComparator(stud_2x6_counts, text_counts_2x6, "Excel Stud 2X6", "Text Stud 2X6")
    common_keys_2x6, unique_to_dict1_2x6, unique_to_dict2_2x6, common_counts_2x6 = comparator_2x6.compare_dictionaries()
    comparator_2x6.plot_bar_chart(common_counts_2x6)
    
    
    # Call function to generate Excel output
    generate_excel_output(stud_2x4_counts, stud_2x6_counts, text_counts_2x4, text_counts_2x6)


if __name__ == "__main__":
    main()
