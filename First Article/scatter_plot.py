import plotly.express as px

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Colour by continent
fig = px.scatter(
    gapminder,
    x="lifeExp",
    y="gdpPercap",
    color="continent",
    labels={
        "gdpPercap": "GDP Per Capita",
        "lifeExp": "Life Expectancy",
    },
    title="Scatter Plot of GDP Per Capita and Life Expectancy",
)
fig.show()
