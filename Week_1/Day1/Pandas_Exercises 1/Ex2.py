import pandas as pd

data = {
	'Name' : ['Aapeli', 'Simeoni', 'Juhani', 'Eemeli', 'Lauri'],
	'Age' : [18, 19, 19, 20, 21],
	'Score' : [7, 8, 9, 9, 10]
}

df = pd.DataFrame(data)

df_indexed = df.set_index(['Name'])
print(df_indexed)