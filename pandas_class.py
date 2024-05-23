import pandas as pd

data = {
    'name': ('aashish', 'deepana', 'milan', 'saroj'),
    'Age': (20, 21, 22, 23),
    'city':('lalitpur', 'kalanki', 'baktapur', 'bafal')
}

df = pd.DataFrame(data)

df = pd.read_csv(r'C:\Users\DELL\Downloads\sample1.csv')

print(df)
