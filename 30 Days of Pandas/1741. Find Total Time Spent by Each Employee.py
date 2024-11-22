import pandas as pd 
data = {
    "emp_id": [1, 1, 1, 2, 2],
    "event_day": ["2020-11-28", "2020-11-28", "2020-12-03", "2020-11-28", "2020-12-09"],
    "in_time": [4, 55, 1, 3, 47],
    "out_time": [32, 200, 42, 33, 74]
}

data = pd.DataFrame(data)
# print(data)

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['diff_in_out'] = employees.out_time - employees.in_time

    results = employees.groupby(['event_day', 'emp_id'])['diff_in_out'].sum().astype(int).reset_index()
    results.rename(columns = {'event_day': 'day', 'diff_in_out' : 'total_time'}, inplace = True)
    return results

print(total_time(data))