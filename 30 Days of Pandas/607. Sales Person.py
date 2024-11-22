 
import pandas as pd 


# sales person data
sales_person_data = {
    "sales_id": [1, 2, 3, 4, 5],
    "name": ["John", "Amy", "Mark", "Pam", "Alex"],
    "salary": [100000, 12000, 65000, 25000, 5000],
    "commission_rate": [6, 5, 12, 25, 10],
    "hire_date": ["4/1/2006", "5/1/2010", "12/25/2008", "1/1/2005", "2/3/2007"]
}
sales_person = pd.DataFrame(sales_person_data)


# Company data
company_data = {
    "com_id": [1, 2, 3, 4],
    "name": ["RED", "ORANGE", "YELLOW", "GREEN"],
    "city": ["Boston", "New York", "Boston", "Austin"]
}

company = pd.DataFrame(data = company_data)

# Orders data
orders_data = {
    "order_id": [1, 2, 3, 4],
    "order_date": ["1/1/2014", "2/1/2014", "3/1/2014", "4/1/2014"],
    "com_id": [3, 4, 1, 1],
    "sales_id": [4, 5, 1, 4],
    "amount": [10000, 5000, 50000, 25000]
}
orders = pd.DataFrame(orders_data)

# print(orders)


import pandas as pd

def sales_person_d(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    RED_id = list(company[company.name == 'RED']['com_id'])[0]
    list_Not_wanted = list(orders[orders.com_id == RED_id]['sales_id'])
    results = sales_person[~sales_person['sales_id'].isin(list_Not_wanted)]
    return results[['name']]


print(sales_person_d(sales_person, company, orders))