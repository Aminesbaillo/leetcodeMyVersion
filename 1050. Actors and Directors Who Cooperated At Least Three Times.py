import pandas as pd 

data = {
    'actor_id': [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp': [0, 1, 2, 3, 4, 5, 6]
}

data = pd.DataFrame(data)

# print(data)

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    results = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    return results[results.timestamp >= 3][['actor_id', 'director_id']]



print(actors_and_directors(data))