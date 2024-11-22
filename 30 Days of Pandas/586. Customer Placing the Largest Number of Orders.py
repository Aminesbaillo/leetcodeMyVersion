import pandas as pd 
data = {
    'order_number': [1, 2, 3, 4, 5],
    'customer_number': [1, 1, 2, 3, 3]
}
data = pd.DataFrame(data = data) 
print('dataframe :') 
print(data)
print('------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------')


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    results = orders.groupby('customer_number')['order_number'].count().reset_index()
    max_order = results[results.order_number == results.order_number.max()]
    return max_order[['customer_number']]

print(largest_orders(data))