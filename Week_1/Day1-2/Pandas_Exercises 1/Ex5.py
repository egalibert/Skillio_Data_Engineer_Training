import pandas as pd

data = {
	'Name' : ['Aapeli', 'Simeoni', 'Juhani', 'Eemeli', 'Lauri'],
	'Age' : [18, 19, 19, 20, 21],
	'Score' : [7, None, 9, 9, None]
}

df = pd.DataFrame(data)
df['Score'] = df['Score'].astype(float)

fil_df = df.fillna(df['Score'].mean())
print(fil_df)
