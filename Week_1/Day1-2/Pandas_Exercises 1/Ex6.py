import pandas as pd

data1 = {
	'Name' : ['Aapeli', 'Simeoni', 'Juhani', 'Eemeli', 'Lauri'],
	'Age' : [18, 19, 19, 20, 21],
	'Score' : [7, 8, 9, 9, 10]
}

data2 = {
	'Name' : ['Risto', 'Urho', 'Mikko', 'Saku', 'Jarkko'],
	'Age' : [31, 33, 41, 16, 30],
	'Occupation' : ['Pilot', 'Developer', "Police", 'Janitor', 'Athlete']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

combined_df = pd.concat([df1, df2])
print(combined_df)