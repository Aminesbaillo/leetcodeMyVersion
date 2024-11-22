import pandas as pd 
data = pd.DataFrame(data = {'product_id' : [0, 1], 
                            'store1' : [95, 70],
                            'store2' : [100, None],
                            'store3' : [105, 80]})

print(data)


def rerrange_product_table(product: pd.DataFrame) -> pd.DataFrame:
    results = pd.melt(product, id_vars = 'product_id', value_vars = ['store1', 'store2', 'store3'], var_name ='store', value_name= 'price')
    results = results.dropna()
    return results

print(rerrange_product_table(data))