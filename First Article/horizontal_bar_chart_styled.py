# Import the libraries we need
import plotly.express as px

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Group by 'year' and calculate the mean of 'lifeExp' and sort in decending
# order
df_grouped1 = (
    gapminder.groupby("continent")["lifeExp"]
    .mean()
    .sort_values(ascending=True)
    .reset_index()
)

# Create the bar chart with 'year' on the x-axis and 'lifeExp' on the y-axis.
# Add labels Dictionary to format the Axes labels
fig = px.bar(
    df_grouped1,
    x="lifeExp",
    y="continent",
    labels={
        "lifeExp": "Life Expectancy (Average)",
        "continent": "Continent",
    },
    title="Average life expectancy by Continent",
)

# Show the figure
fig.show()
