import plotly.express as px
import pandas as pd

# Read in our data to our dataframe 'df'
df = pd.read_csv("../datafiles/taxonomy.csv")

# Count the occurrences of each combination of risks
df_count = (
    df.groupby(["L1 Risk", "L2 Risk", "L3 Risk"]).size().reset_index(name="counts")
)

# Create the sunburst chart
fig = px.sunburst(
    df_count,
    path=["L1 Risk", "L2 Risk", "L3 Risk"],
    values="counts",
    title="Risk Data Displayed on a Sunburst Chart",
)

# Show the figure
fig.show()
