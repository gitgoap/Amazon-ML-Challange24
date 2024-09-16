import pandas as pd
import glob

def merge_predictions(file_list, output_file='test_out.csv'):
    # Initialize a DataFrame with index from 0 to 131287 and prediction as "" for all rows
    merged_df = pd.DataFrame({'index': range(131288), 'prediction': [''] * 131288})
    
    # Loop through each input CSV file
    for file in file_list:
        temp_df = pd.read_csv(file)
        for i, row in temp_df.iterrows():
            index = row['index']
            prediction = row['prediction']
            # Update the prediction in the merged DataFrame for the matching index
            merged_df.loc[merged_df['index'] == index, 'prediction'] = prediction
    
    # Save the output CSV (any index not present in input files will retain "" as prediction)
    merged_df.to_csv(output_file, index=False)

# Example usage:
file_list = glob.glob('*.csv')  # Get all CSV files in the current folder
merge_predictions(file_list)
