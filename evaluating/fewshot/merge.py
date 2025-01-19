import pandas as pd
import os

def combine_csv_columns(file1_path, file2_path, column_to_extract):
    try:
        df1 = pd.read_csv(file1_path)
        df2 = pd.read_csv(file2_path)

        if column_to_extract not in df1.columns:
            raise ValueError(f"Column '{column_to_extract}' not found in the first file.")
        
        if len(df1) != len(df2):
            raise ValueError(f"The number of rows in the two files are not the same")

        df2[column_to_extract] = df1[column_to_extract]
        return df2
    
    except FileNotFoundError as nf:
        print(f"Error: One or both files not found. {nf}")
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == '__main__':
    dataset_name = "Irf_belong"
    column_to_extract = 'gemini20flashexp'
    from_file1_path = os.path.join('evaluating', f'fs_{column_to_extract}', f'{dataset_name}.csv')
    to_file2_path = os.path.join('evaluating', 'fewshot', f'{dataset_name}.csv')

    modified_df = combine_csv_columns(from_file1_path, to_file2_path, column_to_extract)

    if modified_df is not None:
        output_path = os.path.join(os.path.dirname(to_file2_path), f'{dataset_name}.csv')
        modified_df.to_csv(output_path, index=False)
