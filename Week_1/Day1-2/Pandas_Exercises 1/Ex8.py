import pandas as pd

data = {
	'Date' : ['1996-01-27', '2008-06-08', '1995-09-12', '1996-02-08']
}

df = pd.DataFrame(data)
print(df.dtypes)

df['Date'] = pd.to_datetime(df['Date'])
print('\n')

print(df.dtypes)