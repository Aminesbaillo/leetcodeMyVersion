import pandas as pd

# Création de la table Employee
employee_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}

employee_table = pd.DataFrame(employee_data)

# Création de la table Department
department_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}

department_table = pd.DataFrame(department_data)



# # departement highest salary 
## SOLUTION : 

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the highest salary for each department in the given DataFrames.

    Args:
        employee: A DataFrame with columns 'id', 'name', 'salary', and 'departmentId'.
        department: A DataFrame with columns 'id' and 'name'.

    Returns:
        A DataFrame with columns 'Department', 'Employee', and 'Salary' showing the highest salary for each department.
    """

    # Merge DataFrames based on department ID
    merged_data = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))

    # Drop unnecessary columns
    merged_data.drop(columns=['id_department', 'departmentId'], inplace=True)

    # Rename columns for clarity
    merged_data.rename(columns={'name_department': 'Department', 'name_employee': 'Employee', 'salary': 'Salary'}, inplace=True)

    # Find the maximum salary for each department
    merged_data['max_salary'] = merged_data.groupby('Department')['Salary'].transform('max')

    # Filter for rows with the maximum salary
    filtered_data = merged_data[merged_data['Salary'] == merged_data['max_salary']]

    # Select the desired columns
    return filtered_data[['Department', 'Employee', 'Salary']]

# Example usage:
# Assuming you have employee_table and department_table DataFrames
result = department_highest_salary(employee_table, department_table)
print(result)