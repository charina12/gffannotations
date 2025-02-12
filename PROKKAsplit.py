import pandas as pd

# path to .csv file with one column named "annotations"
x = 
# path to write csv
out = 

df = pd.read_csv(x)

# create function to split row's string into a dictionary
def split_row_to_dict(row):
    key_value_pairs = row.split(';') #split input into factors, separated by ;
    return {kv.split('=')[0]: kv.split('=')[1] for kv in key_value_pairs} #create columns with before = as colname and after = as value


# create new dataframe by applying defined function to column of interest
anno = pd.DataFrame(df['annotation'].apply(split_row_to_dict).tolist())
# join with original data, keeps annotation column to reference
new_df = df.join(anno)
# write csv
new_df.to_csv(out)
