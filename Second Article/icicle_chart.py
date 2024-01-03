import plotly.express as px
import pandas as pd

# Read in our data to our datafeame 'df'
df = pd.read_csv("../datafiles/taxonomy.csv")

# Count the occurrences of each combination of risks
df_count = (
    df.groupby(["L1 Risk", "L2 Risk", "L3 Risk"]).size().reset_index(name="counts")
)

# Create the icicle chart
fig = px.icicle(
    df_count,
    path=["L1 Risk", "L2 Risk", "L3 Risk"],
    values="counts",
    title="Operational Risk Data",
)

# Set the 'root' colour and some margins
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Set text position to inside the slice and format the text
fig.update_traces(
    textinfo="label+value",
    texttemplate="%{label}:<br> Risks: %{value:.0f}",
)

# Set the chart size to 900 x 1250 pixels and disable the legend
fig.update_layout(autosize=False, width=900, height=1250)


# Display our Chart
fig.show()
