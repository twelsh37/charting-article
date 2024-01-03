# Import the necessary module from the plotly library
import plotly.graph_objects as go
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

# Create an empty figure
fig = go.Figure()

# Loop over the DataFrame, grouping it by the "Continent" column
for continent, group in df.groupby("Continent"):
    # For each group, loop over the DataFrame again, this time grouping it by the "City" column
    for city, city_group in group.groupby("City"):
        # Add a bar to the figure for each city in the current continent group
        fig.add_trace(
            go.Bar(
                # Set the x-values to the continent of the current city group
                x=city_group["Continent"],
                # Set the y-values to the "Entities" column of the current city group
                y=city_group["Entities"],
                # Set the name of the bar to the current city (this will be displayed in the legend)
                name=city,
                # Set the hover template to display the city, continent, and entities when a user hovers over a bar
                hovertemplate="City=%s<br>Continent=%s<br>Entities=%%{y}<extra></extra>"
                % (city, continent),
            )
        )

# Set the title of the legend to "City"
fig.update_layout(legend_title_text="City")

# Set the graph title
fig.update_layout(title="Chart created by plotly.graph_objects")

# Set the title of the x-axis to "Continent"
fig.update_xaxes(title_text="Continent")

# Set the title of the y-axis to "Entities"
fig.update_yaxes(title_text="Entities")

# Display the figure
fig.show()