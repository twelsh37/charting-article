import plotly.express as px
import pandas as pd

# create our dataframe
df = pd.DataFrame(
    dict(process=["Website", "Product", "Purchase", "Ship"], counts=[100, 75, 35, 35])
)

# Create our Funnel Area Chart
fig = px.funnel_area(
    df,
    names="process",
    values="counts",
    title="Funnel Area chart",
)

# Set text position to inside the slice and format the text
fig.update_traces(
    textposition="inside",
    textinfo="label+percent+value",
    texttemplate="<b>%{label}</b><br> Customers to reach this point: %{value:.0f}<br> (%{percent:.0%})",
)

# Set the chart size to 800 x 800 pixels and disable the legend
fig.update_layout(showlegend=False, autosize=False, width=800, height=800)

# Display our Chart
fig.show()