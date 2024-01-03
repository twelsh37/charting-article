import plotly.express as px

# setup our gapminder dataset
gapminder = px.data.gapminder()

# Get data only for Afghanistan
afghanistan_2007 = gapminder.query("country == 'Afghanistan'")

# Afghanistan_2007 DataFrame with our filtered Afghanistan data
fig = px.pie(
    afghanistan_2007,
    values="lifeExp",
    names="year",
    title="Life Expectancy growth in Afghanistan 1952 - 2007",
)

# Create a doughnut chart by specifying a hole size
fig.update_traces(hole=0.4)

# Set text position to inside the slice and format the text
fig.update_traces(
    textposition="inside",
    textinfo="label+percent+value",
    texttemplate="%{label}: %{value:.0f} (%{percent:.0%})",
)

# Pull out the slice for the year 2007
pull_values = [0.2 if year == 2007 else 0 for year in afghanistan_2007["year"]]
fig.update_traces(pull=pull_values)

# Set the chart size to 800 x 800 pixels and disable the legend
fig.update_layout(showlegend=False, autosize=False, width=800, height=800)

# Add an annotation to the center of the chart
fig.add_annotation(
    text=" Some text here",
    x=0.5,
    y=0.5,
    showarrow=False,
    font_size=20,
    opacity=0.7,
)

# Show the figure
fig.show()