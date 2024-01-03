import pandas as pd
import plotly.express as px

# DATASET - https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

# read in our dataset
salary_df = pd.read_csv('../datafiles/ds_salaries.csv')

# filter the dataframe based on the country we want to plot
country_df = salary_df[salary_df['company_location'].isin(['US', 'GB', 'IN'])].copy()

# plot our box plot
box = px.box(country_df,
             x = 'company_location',
             y = 'salary_in_usd',
             color = 'company_location',
             labels={
                 "salary_in_usd": "Salary (USD)",
                 "company_location": "Country",
                 },
             title = ' Salary comparison for Data Scientists from US, GB and IN'
            )

# Set the chart size to 1000 x 1000 pixels and disable the legend
box.update_layout(showlegend=False, autosize=False, width=1000, height=1000)

box.show()
