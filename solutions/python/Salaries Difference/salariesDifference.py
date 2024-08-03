# Import your libraries
import pandas as pd

# joining data of two data frames to collectively form a single dataframe
df = pd.merge(
    db_employee,
    db_dept,
    how="left",
    left_on=['department_id'],
    right_on=['id'],
)

# seggregating the engineering data
df_engineering = df[df['department'] == "engineering"]
# grouping data based on department and fetching the max salary out of it
df_engineering_salary = df_engineering.groupby('department')['salary'].max().reset_index(name = 'engineering_salary')


# seggregating the marketing data
df_marketing = df[df['department'] == 'marketing']
# grouping data based on department and fetching the max salary out of it
df_marketing_salary = df_marketing.groupby('department')['salary'].max().reset_index(name = 'marketing_salary')


# result making
result = abs(pd.DataFrame(df_marketing_salary['marketing_salary'] - df_engineering_salary['engineering_salary']))
result
