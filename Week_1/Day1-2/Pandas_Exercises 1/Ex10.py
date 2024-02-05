import pandas as pd

data = {
	'Score' : [1, 1, 1, 1, 2, 2, 3]
}

df = pd.DataFrame(data)
print(df['Score'].unique())