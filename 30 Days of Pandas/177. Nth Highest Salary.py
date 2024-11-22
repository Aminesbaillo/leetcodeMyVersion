import pandas as pd 
case_1 = pd.DataFrame(data = {'id': [1, 2, 3],
                            'salary': [100, 200, 300]})

case_2 = pd.DataFrame(data = {'id': [1], 'salary': [100]})

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if employee.shape[0] < N or N <= 0 :
        return pd.DataFrame(data = {f'getNthHighestSalary ({N})': [None]})

    else :
        unique_employee = employee['salary'].drop_duplicates().sort_values(ascending = False).reset_index(drop = True)
        return pd.DataFrame(data = {f'getNthHighestSalary ({N})':[ employee.iloc[N-1]['salary']]})
    
print(nth_highest_salary(case_1, 2))
print(nth_highest_salary(case_2, 2))