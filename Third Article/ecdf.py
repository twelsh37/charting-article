import pandas as pd
import plotly.express as px

# DATASET - https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

# read in our dataset
salary_df = pd.read_csv('../datafiles/ds_salaries.csv')

# filter the dataframe based on the country we want to plot
country_df = salary_df[salary_df['company_location'].isin(['US', 'GB', 'IN'])].copy()

ecdf = px.ecdf(country_df, x='salary_in_usd')

# Set the chart size to 800 x 800 pixels
ecdf.update_layout(width=800, height=800)

ecdf.show()
