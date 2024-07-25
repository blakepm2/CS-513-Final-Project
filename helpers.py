import pandas as pd

def read_in_data():
    dfs = []
    for file in ('Dish', 'Menu', 'MenuItem', 'MenuPage'):
        dfs.append(pd.read_csv(f'data/{file}.csv'))
    return dfs