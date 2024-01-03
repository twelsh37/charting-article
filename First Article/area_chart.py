# Import the Plotly Express library
import plotly.express as px

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Create an area chart using the gapminder dataset
# The x-axis represents the year
# The y-axis represents the GDP per Capita
# Different continents are represented by different colors
# Each line group represents a country
# The labels are customized to "GDP Per Capita" for gdpPercap and "Year" for year
# The title of the chart is set to "Rise in GDP Per Capita,  1952 - 2007"
fig = px.area(
    gapminder,
    x="year",
    y="gdpPercap",
    color="continent",
    line_group="country",
    labels={
        "gdpPercap": "GDP Per Capita",
        "year": "Year",
    },
    title="Rise in GDP Per Capita,  1952 - 2007",
)

# The background color of the plot is updated to transparent
fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)")

# Display the figure
fig.show()
