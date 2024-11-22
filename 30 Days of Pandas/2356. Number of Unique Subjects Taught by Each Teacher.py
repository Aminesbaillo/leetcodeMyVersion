import pandas as pd
data = {
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id': [3, 4, 3, 1, 1, 1, 1]    
}
data = pd.DataFrame(data= data)
# print(data)

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    results = teacher.drop_duplicates(subset=['teacher_id', 'subject_id'], keep = 'first')
    results = results.groupby('teacher_id')['subject_id'].count().reset_index()
    results.rename(columns = {'subject_id': 'cnt'}, inplace = True)
    return results[['teacher_id', 'cnt']]
    # return results

print(count_unique_subjects(data))