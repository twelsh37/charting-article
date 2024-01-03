import pandas as pd
import plotly.express as px

# DATASET - https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

# read in our dataset
salary_df = pd.read_csv('../datafiles/ds_salaries.csv')

# filter the dataframe based on the country we want to plot
country_df = salary_df[salary_df['company_location'].isin(['US', 'GB', 'IN'])].copy()

violin = px.violin(country_df,
                   x='company_location',
                   y='salary_in_usd',
                   labels={
                       "salary_in_usd": "Salary (USD)",
                       "company_location": "Country",
                       },
                   color='company_location',
                   title=' Salary comparison for Data Scientists from US, GB and IN')
violin.update_layout(showlegend=False, autosize=False, width=800, height=800)

violin.show()
