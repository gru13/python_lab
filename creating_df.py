import pandas as pd

# create a DataFrame with the given data
data = {'NAME': ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn'],
        'ROLL NO': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        'THEORY': [97, 98, 93, 94, 92, 0, 97, 93, 90, 100, 96, 95, 100, 91],
        'PRACTICALS': [10, 10, 10, 10, 98, 0, 10, 10, 10, 10, 10, 10, 10, 10],}

df = pd.DataFrame(data)

# export the DataFrame to a CSV file with integers
df.to_csv('./data/Pandadata1.csv', index=False)