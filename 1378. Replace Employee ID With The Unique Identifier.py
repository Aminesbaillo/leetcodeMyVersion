 
import pandas as pd 
employees_data  = {
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
}
employees = pd.DataFrame(data = employees_data)

employee_uni_data = {
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
}
employee_uni = pd.DataFrame(data= employee_uni_data )

print("=====================================")
print(employees)

print("=====================================")
print(employee_uni)

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    results = pd.merge(employee_uni, employees, on ='id', how = 'right')
    results.fillna('null', inplace = True)
    return results[['unique_id', 'name']]

print(replace_employee_id(employees, employee_uni))