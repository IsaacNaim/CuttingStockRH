import pandas as pd
from functions.dictionary_comparator import DictionaryComparator

def generate_excel_output(stud_2x4_counts, stud_2x6_counts, text_counts_2x4, text_counts_2x6):
    # Compare dictionaries
    comparator_2x4 = DictionaryComparator(stud_2x4_counts, text_counts_2x4, "Excel Stud 2X4", "Text Stud 2X4")
    common_keys_2x4, unique_to_dict1_2x4, unique_to_dict2_2x4, common_counts_2x4 = comparator_2x4.compare_dictionaries()

    comparator_2x6 = DictionaryComparator(stud_2x6_counts, text_counts_2x6, "Excel Stud 2X6", "Text Stud 2X6")
    common_keys_2x6, unique_to_dict1_2x6, unique_to_dict2_2x6, common_counts_2x6 = comparator_2x6.compare_dictionaries()

    # Create summary DataFrame
    summary_data = {
        "Comparison Type": ["Excel Stud 2X4 vs Text Stud 2X4", "Excel Stud 2X6 vs Text Stud 2X6"],
        "Common Keys": [len(common_keys_2x4), len(common_keys_2x6)],
        "Unique to Excel": [len(unique_to_dict1_2x4), len(unique_to_dict1_2x6)],
        "Unique to Text": [len(unique_to_dict2_2x4), len(unique_to_dict2_2x6)]
    }
    summary_df = pd.DataFrame(summary_data)

    # Create detailed DataFrames for each dictionary
    def create_detailed_dataframe(keys_values_dict, sheet_name):
        keys_values_df = pd.DataFrame(keys_values_dict.items(), columns=[f"{sheet_name} Keys", f"{sheet_name} Values"])
        return keys_values_df

    detail_df_2x4_excel = create_detailed_dataframe(stud_2x4_counts, "Stud 2X4 Excel")
    detail_df_2x6_excel = create_detailed_dataframe(stud_2x6_counts, "Stud 2X6 Excel")
    detail_df_2x4_text = create_detailed_dataframe(text_counts_2x4, "Stud 2X4 Text")
    detail_df_2x6_text = create_detailed_dataframe(text_counts_2x6, "Stud 2X6 Text")

    # Write to Excel
    output_file_path = 'outputfiles/comparison_results.xlsx'
    with pd.ExcelWriter(output_file_path) as writer:
        summary_df.to_excel(writer, sheet_name='Summary', index=False)

        # Write detailed DataFrames to 'Details' sheet with proper formatting
        start_row = 0
        start_col = 0
        
        # Write Excel dictionaries
        detail_df_2x4_excel.to_excel(writer, sheet_name='Details', startrow=start_row, startcol=start_col, index=False)
        detail_df_2x6_excel.to_excel(writer, sheet_name='Details', startrow=start_row, startcol=start_col + len(detail_df_2x4_excel.columns) + 1, index=False)

        # Calculate start row for text dictionaries
        start_row = len(detail_df_2x4_excel) + 2

        # Write Text dictionaries
        detail_df_2x4_text.to_excel(writer, sheet_name='Details', startrow=start_row, startcol=start_col, index=False)
        detail_df_2x6_text.to_excel(writer, sheet_name='Details', startrow=start_row, startcol=start_col + len(detail_df_2x4_text.columns) + 1, index=False)

    print(f"Results written to {output_file_path}")

# Example usage (for testing purposes):
if __name__ == "__main__":
    from functions.data_processor import ExcelDataProcessor, TextDataProcessor

    # Example usage for .xlsx file
    excel_file_path = 'inputfiles/Wastage - v6.xlsx'  # Replace with your file path
    excel_processor = ExcelDataProcessor()
    stud_2x4_counts, stud_2x6_counts = excel_processor.read_excel_file(excel_file_path)

    # Example usage for .txt files
    txt_file_path_2x4 = 'inputfiles/Stud_2_4_12_combined.txt'  # Replace with your file path
    txt_processor = TextDataProcessor()
    text_counts_2x4 =  txt_processor.process_txt_file(txt_file_path_2x4)

    txt_file_path_2x6 = 'inputfiles/Stud_2_6_12_combined.txt'  # Replace with your file path
    text_counts_2x6 = txt_processor.process_txt_file(txt_file_path_2x6)

    # Generate Excel output
    generate_excel_output(stud_2x4_counts, stud_2x6_counts, text_counts_2x4, text_counts_2x6)
