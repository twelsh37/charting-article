import plotly.express as px

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Mask our data so we only get Afghanistan
mask = gapminder["country"] == "Afghanistan"

# Create our Scatter plot
fig = px.scatter(
    gapminder[mask],
    x="lifeExp",
    y="gdpPercap",
    # add in size as the third variable
    size="pop",
    # Set the maximum marker size
    size_max=60,
    labels={
        "gdpPercap": "GDP Per Capita",
        "lifeExp": "Life Expectancy",
    },
    title="Bubble Chart depicting Afghan Life expectancy vs GDP Per Capita",
)
fig.show()
