import pandas as pd 

data = pd.DataFrame(data = {'account_id': [3, 2, 8, 6], 
                            'income' : [108939, 12747, 87709, 91796]})
print(data)

def count_salary_categories(account: pd.DataFrame) -> pd.DataFrame:

    all_categories = ["Low Salary", "Average Salary", "High Salary"]


    # Categorize salaries into Low, Average, and High
    account['category'] = account['income'].apply(
        lambda salary: "Low Salary" if salary < 20000 else (
            "High Salary" if salary > 50000 else "Average Salary"
        )
    )
    # Group by category and count occurrences
    results = account.groupby('category')['income'].count().reset_index()
    print(results)
    results.rename(columns={'income': 'accounts_count'}, inplace=True)

    # Ensure all categories are represented, even if their count is 0
    full_results = pd.DataFrame({'category': all_categories}).merge(
        results, on='category', how='left'
    )
    full_results['accounts_count'] = full_results['accounts_count'].fillna(0).astype(int)
    
    return full_results


print(count_salary_categories(data))