import numpy
import pandas as pd

data = {
	'Name' : ['Aapeli', 'Simeoni', 'Juhani', 'Eemeli', 'Lauri'],
	'Age' : [18, 19, 19, 20, 21],
	'Score' : [7, 8, 9, 9, 10]
}

df = pd.DataFrame(data)
print(df) #EX 1

df_indexed = df.set_index(['Name'])
print(df_indexed) #EX 2

df['Score'] = df['Score'].astype(float)
print(df) #EX 3

df_grouped = df.groupby('Age').mean('Score')
print(df_grouped) # EX 4

