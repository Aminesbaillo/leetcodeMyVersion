 
import pandas as pd 

data = {
    'sell_date': [
        '2020-05-30', '2020-06-01', '2020-06-02', 
        '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'
    ],
    'product': [
        'Headphone', 'Pencil', 'Mask', 
        'Basketball', 'Bible', 'Mask', 'T-Shirt'
    ]
}

data = pd.DataFrame(data = data)

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    results = activities.groupby('sell_date').agg(num_sold = ('product', 'count'), products = ('product', (lambda x: ','.join(sorted(x))))).reset_index()
    return results
print(categorize_products(data))