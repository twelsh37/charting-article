import plotly.express as px

# setup our gapminder dataset
gapminder = px.data.gapminder()

# Get data only for Afghanistan
afghanistan_2007 = gapminder.query("country == 'Afghanistan'")

# afghanistan_2007 DataFrame with our filtered Afghanistan data
fig = px.pie(afghanistan_2007, values="lifeExp", names="lifeExp")

# Show the figure
fig.show()
