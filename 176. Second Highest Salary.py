import pandas as pd 

case_1 = pd.DataFrame(data = {'id' : [1, 2], 'salary': [100, 100]})

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset = 'salary', keep = 'first')
    if employee.shape[0] < 2:
        return pd.DataFrame(data = {'SecondHighestSalary' : [None]})
    else :
        employee = employee.sort_values(by = 'salary', ascending = True).reset_index(drop = True)
        return pd.DataFrame(data = {'SecondHighestSalary' : [employee.iloc[1]['salary']]})
    

print(second_highest_salary(employee=case_1))
