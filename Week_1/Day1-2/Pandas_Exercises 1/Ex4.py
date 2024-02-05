import pandas as pd

data = {
	'Name' : ['Aapeli', 'Simeoni', 'Juhani', 'Eemeli', 'Lauri'],
	'Age' : [18, 19, 19, 20, 21],
	'Score' : [7, 8, 9, 9, 10]
}

df = pd.DataFrame(data)

df_grouped = df.groupby('Age').mean('Score')
print(df_grouped)