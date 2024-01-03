import plotly.express as px
import pandas as pd

# Read in our data to our datafeame 'df'
df = pd.read_csv("../datafiles/taxonomy.csv")

# Count the occurrences of each combination of risks
df_count = (
    df.groupby(["L1 Risk", "L2 Risk", "L3 Risk"]).size().reset_index(name="counts")
)

# Create the Treemap chart
fig = px.treemap(
    df_count,
    path=["L1 Risk", "L2 Risk", "L3 Risk"],
    values="counts",
    title="Risk Data",
    color="counts",
    color_continuous_scale='Blues'
    )

# Set the 'margins for the treemap
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Set text position to inside the slice and format the text
fig.update_traces(
    marker=dict(cornerradius=15),
    textinfo="label+value",
    texttemplate="%{label}:<br> Risks: %{value:.0f}"
    )

# Set the chart size to 900 x 850 pixels and disable the legend
fig.update_layout(autosize=False, width=900, height=650)

" Display our Chart"
fig.show()
