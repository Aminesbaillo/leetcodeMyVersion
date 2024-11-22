import pandas as pd 
data = pd.DataFrame(data = {'id' : [i for i in range(1, 7)], 
                           'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]})
print(data)

def order_score(scores : pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False).astype(int)
    results = scores.sort_values(by = 'score', ascending = False).reset_index()
    return results[['score', 'rank']]

print(order_score(data))