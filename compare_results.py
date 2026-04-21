import pandas as pd

# Load the csv files
phising_df= pd.read_csv('uploads/phising.csv')
predicted_df = pd.read_csv('predictions/predicted_file.csv')

# ensure both dataframes have the result column
if 'Result' not in phising_df.columns or 'Result' not in predicted_df.columns:
    raise ValueError("Both CSV file must contain a 'Result' column")

# Replace -1 with 0 in both dataframes
phising_df['Result']= phising_df['Result'].replace(-1,0)
predicted_df['Result']= predicted_df['Result'].replace(-1,0)

# Calculate the number of matching values
matching_values= (phising_df['Result']==predicted_df['Result']).sum()

# Calculate the total number of rows
total_rows= len(phising_df)

print("Total Rows:",total_rows)
print("Matching Values:",matching_values)

# Calculate the accuracy score
accuracy_score= matching_values/total_rows

print(f"Accuracy Score: {accuracy_score:.2f}")