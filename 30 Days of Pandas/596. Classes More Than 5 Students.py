import pandas as pd 

data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
}

data = pd.DataFrame(data = data)
print(data)


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    results = courses.groupby('class')['student'].count().reset_index()
    results = results[results['student'] > 5]
    return results[['class']]

print(find_classes(data))