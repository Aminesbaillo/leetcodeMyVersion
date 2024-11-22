import pandas as pd 

data = {
    'date_id': [
        '2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7',
        '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'
    ],
    'make_name': [
        'toyota', 'toyota', 'toyota', 'toyota', 'toyota',
        'honda', 'honda', 'honda', 'honda', 'honda'
    ],
    'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
    'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
}
data = pd.DataFrame(data = data) 

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    
    results = daily_sales.groupby(['date_id', 'make_name']).agg(unique_leads= ('lead_id', 'nunique'), unique_partners = ('partner_id', 'nunique')).reset_index()
    return results[['date_id', 'make_name', 'unique_leads', 'unique_partners']]

print(daily_leads_and_partners(data))