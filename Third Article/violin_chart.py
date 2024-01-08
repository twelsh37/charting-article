import pandas as pd
import plotly.express as px


df2 = pd.read_csv('../datafiles/violin_data.csv')
# read in our CSV
violin = px.violin(df2,
                   x = 'Category',
                   y  = 'Value',
                   color = 'Category',
                   title = ' Salary comparison for Data Scientists from US, GB and IN')
violin.update_layout(showlegend=False, autosize=False, width=800, height=800)
violin.show()