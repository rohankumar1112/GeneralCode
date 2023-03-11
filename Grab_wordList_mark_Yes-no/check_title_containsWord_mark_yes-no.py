import pandas as pd

# Load word list
with open('data.txt', 'r') as f:
    wordlist = f.read().splitlines()

# Load Excel file
df = pd.read_csv('mainData.csv') #xlsx

# Specify column to search
column_name = 'title'

# Create a new column for the result
df['Word Match'] = ''

# Iterate over rows and search for matches
for i, row in df.iterrows():
    sentence = str(row[column_name])
    if any(word in sentence for word in wordlist):
        df.at[i, 'Word Match'] = 'Yes'
    else:
        df.at[i, 'Word Match'] = 'No'

# Save the updated Excel file
df.to_csv('check_yes-no_wordList.csv', index=False)