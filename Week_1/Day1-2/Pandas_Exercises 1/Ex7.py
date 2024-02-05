import pandas as pd

data1 = {
	'ID' : [1, 2, 3, 4, 5],
	'Name' : ['Aapeli', 'Simeoni', 'Juhani', 'Eemeli', 'Lauri'],
	'Age' : [18, 19, 19, 20, 21],
}

data2 = {
	'ID' : [1, 2, 3, 4, 5],
	'Salary' : [100000, 60000, 45000, 35000, 120000],
	'Occupation' : ['Pilot', 'Developer', "Police", 'Janitor', 'Athlete']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2)
print(merged_df)