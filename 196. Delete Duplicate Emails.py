import pandas as pd 
data = pd.DataFrame(data = {'id' : [i for i in range(1, 4)], 
                            'email': ['john@example.com', 'bob@example.com', 'john@example.com']})
print(data)

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort by 'id' in ascending order
    person.sort_values(by='id', inplace=True)
    # Drop duplicate emails, keeping the first occurrence
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    return person
print(delete_duplicate_emails(data))