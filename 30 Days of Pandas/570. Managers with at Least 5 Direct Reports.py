import pandas as pd


employee = pd.DataFrame(data = {
    "id": [101, 102, 103, 104, 105, 106],
    "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
    "department": ["A", "A", "A", "A", "A", "B"],
    "managerId": [None, 101, 101, 101, 101, 101],
})

print('employee')
print(employee)
print('================================================================')
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    results = employee.groupby('managerId').agg(supervizedNum = ('id', 'count')).reset_index()
    l = list(results.managerId.astype(int))
    return employee[employee['id'].isin(l) & employee['managerId'].isnull()][['name']]
print(find_managers(employee))