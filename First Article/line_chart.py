import plotly.express as px

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Mask our data so we only get Afghanistan
mask = gapminder["country"] == "Afghanistan"

# Create the line chart with 'year' on the x-axis and 'lifeExp' on the y-axis.
# Add labels Dictionary to format the Axes labels
# Add an update_layout to set the plot background colour to transparent
fig = px.line(
    gapminder[mask],
    x="year",
    y="lifeExp",
    labels={
        "lifeExp": "Life Expectancy",
        "year": "Year",
    },
    title="Rise In Life Expectancy, Afghanistan 1952 - 2007",
).update_layout(plot_bgcolor="rgba(0, 0, 0, 0)")

# Show the figure
fig.show()
