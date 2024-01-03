# Import the libraries we need
import plotly.express as px
import pandas as pd

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Group by 'year' and calculate the mean of 'lifeExp and sort in accending order'
df_grouped1 = (
    gapminder.groupby("continent")["lifeExp"]
    .mean()
    .sort_values(ascending=True)
    .reset_index()
)

# Create the bar chart with 'continent' on the x-axis and 'lifeExp' on the y-axis
fig = px.bar(df_grouped1, x="continent", y="lifeExp")

# Show the figure
fig.show()