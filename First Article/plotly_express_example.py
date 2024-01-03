# Chart created using Plotly Express

# Import the necessary module from the plotly library
import plotly.express as px
import pandas as pd

# Create our Pandas dataframe with some data to work with
df = pd.DataFrame(
    {
        "Continent": [
            "Africa",
            "Antarctica",
            "Asia",
            "Australia",
            "Europe",
            "North America",
            "South America",
        ],
        "City": [
            "Nairobi",
            "Haley",
            "Shanghai",
            "Sydney",
            "London",
            "Seattle",
            "Caracas",
        ],
        "Entities": [24, 12, 76, 29, 62, 45, 57],
    }
)

# Create a bar chart using the DataFrame `df`, with "Continent" as the -values,
# "Entities" as the y-values, and "City" as the color of the bars. Finally we set
# the Graph title to 'title = '
fig = px.bar(
    df,
    x="Continent",
    y="Entities",
    color="City",
    title="Chart created by plotly.express",
)

# Display the figure
fig.show()
