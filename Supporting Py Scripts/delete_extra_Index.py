import pandas as pd

def remove_rows(csv_file):
    # List of indices to remove
    indices_to_remove = {
        4613, 121862, 33803, 33804, 33805, 25115, 25116, 124444, 124445,
        108082, 108083, 17479, 17480, 3150, 54862, 47185, 18514, 18515,
        104531, 71253, 88676, 119400, 119401, 34922, 19567, 19568, 21619,
        21620, 21621, 127615, 120450, 120451, 127110, 43657, 101003, 64168,
        15540, 15541, 55990, 122084, 69367, 69368, 69369, 15098, 1787, 763,
        1788, 3842, 34057, 120077, 20238, 20239, 16144, 120078, 124692,
        124693, 3864, 3865, 8480, 31018, 31019, 15662, 63792, 120112, 120113,
        2871, 63807, 18752, 64848, 109399, 75610, 75611, 75612, 112480, 121198,
        16751, 121199, 63346, 63347, 24950, 24951, 62330, 66951, 66952, 1950,
        36254, 36255, 10662, 86447, 86448, 89529, 89530, 27580, 129532, 73662,
        128461, 39917, 129531, 58364, 58365, 58366
    }

    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Filter out rows where the 'index' column value is in the indices_to_remove set
    filtered_df = df[~df['index'].isin(indices_to_remove)]

    # Save the updated DataFrame back to the CSV file (overwrite)
    filtered_df.to_csv(csv_file, index=False)

# Example usage:
csv_file = 'test_out.csv'  # Replace with your file path if needed
remove_rows(csv_file)
