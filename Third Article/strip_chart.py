import pandas as pd
import plotly.express as px

# read in our dataset
salary_df = pd.read_csv('../datafiles/ds_salaries.csv')

# filter the dataframe based on the country we want to plot
country_df = salary_df[salary_df['company_location'].isin(['US', 'GB', 'IN'])].copy()

fig = px.strip(country_df,
               x='salary_in_usd',
               y='company_location',
               labels={
                   "salary_in_usd": "Salary (USD)",
                   "company_location": "Country",
               },
               color='company_location',
               title=' Salary comparison for Data Scientists from US, GB and IN')

fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)", width=800, height=800)
fig.show()