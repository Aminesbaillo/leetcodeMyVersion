import pandas as pd


students = {
    "student_id": [1, 2, 13, 6],
    "student_name": ["Alice", "Bob", "John", "Alex"]
}
students = pd.DataFrame(data = students)

subjects = {
    "subject_name": ["Math", "Physics", "Programming"]
}
subjects = pd.DataFrame(data = subjects)

examinations ={
    "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
    "subject_name": [
        "Math", "Physics", "Programming", "Programming", "Physics",
        "Math", "Math", "Programming", "Physics", "Math", "Math"
    ]
}
examinations = pd.DataFrame(data = examinations)

# print(examinations)
# def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
#     results_1 = pd.merge(examinations, subjects, how= "left", on="subject_name")
#     results_2 = pd.merge(students, results_1, how= "left", on="student_id")

#     results = results_2.groupby(['student_id', 'subject_name', 'student_name']).size()
#     return results


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_combinations = pd.merge(students.assign(j = 1),subjects.assign(j = 1), on = 'j').drop('j', axis=1)
    attended_df = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams =('subject_name', 'count')).reset_index()
    results = pd.merge(all_combinations, attended_df, on = ['student_id', 'subject_name'], how = 'left').sort_values(by= ['student_id', 'subject_name'], ascending = True)
    results.attended_exams = results.attended_exams.fillna(0).astype(int)

    return results[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    
print(students_and_examinations(students, subjects, examinations) )