import plotly.express as px
import pandas as pd

# read in our dataset
salary_df = pd.read_csv('../datafiles/ds_salaries.csv')

# filter the dataframe based on the country we want to plot
country_df = salary_df[salary_df['company_location'].isin(['US', 'GB', 'IN'])].copy()

fig = px.ecdf(country_df,
              x = 'salary_in_usd',
              labels={
                  "salary_in_usd": "Salary (USD)",
                  "company_location": "Country",
                  },
              markers=False,
              lines=True,
              marginal="histogram",
             )
# The background color of the plot is updated to transparent
fig.update_layout(width=800, height=800)

fig.show()
