import pandas as pd
import plotly.express as px

# DATASET - https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

# read in our dataset
salary_df = pd.read_csv('../datafiles/ds_salaries.csv')

# filter the dataframe based on the country and job title we want to plot
country_job_df = salary_df[(salary_df['company_location'].isin(['US', 'GB', 'IN'])) &
                           (salary_df['job_title'].isin(['Data Scientist', 'Big Data Engineer']))].copy()
# plot our box plot
box = px.box(country_job_df,
             x='company_location',
             y='salary_in_usd',
             color='company_location',
             # create a separate plot for each job title
             facet_col='job_title',
             labels={
                 "salary_in_usd": "Salary (USD)",
                 "company_location": "Country",
             },
             title='Salary comparison for Big Data Engineer and Data Scientist from USA, GB, and India'
             )

# Remove "job_title=" from facet column titles using a nice lamda function
# to split the text of each annotation at the equals sign and keep only
# the part after it
box.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

# Set the chart size to 1000 x 1000 pixels and disable the legend
box.update_layout(showlegend=False, autosize=False, width=1000, height=1000)

box.show()
